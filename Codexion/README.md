*This project has been created as part of the 42 curriculum by nweber--.*

# Codexion

## Description

Codexion is a C concurrency simulation in which coders compete for USB dongles
needed to compile. Each coder runs in its own POSIX thread. To compile, a coder
must acquire both adjacent dongles; after compiling, the coder debugs and
refactors before requesting dongles again, except after its final required
compile.

The simulation supports two dongle-request scheduling modes:

- `fifo`: requests are served in arrival order.
- `edf`: requests are ordered by their burnout deadline
  (`last_compile_start + time_to_burnout`).

A monitor thread checks coder deadlines. The simulation ends when a coder burns
out or when every coder has completed the required number of compilations.
Messages report dongle acquisition and coder state changes in milliseconds
since the simulation started.

## Instructions

### Compilation

Build the program from the repository root:

```sh
make
```

The Makefile uses `cc` with `-Wall -Wextra -Werror -pthread`. The available
targets are:

```sh
make all
make clean
make fclean
make re
```

### Execution

Run the program with all eight arguments, in this order:

```sh
./codexion number_of_coders time_to_burnout time_to_compile \
	time_to_debug time_to_refactor number_of_compiles_required \
	dongle_cooldown scheduler
```

All time values are in milliseconds. Use non-negative integer values and a
positive number of coders. `scheduler` must be exactly `fifo` or `edf`.

Example:

```sh
./codexion 5 800 100 100 100 3 20 fifo
```

## Blocking cases handled

- **Concurrent access to dongles:** each dongle has its own mutex. A coder
  checks that it is at the head of both dongle request queues and that both
  dongles are free before marking them as used.
- **Conflicting acquisition and release operations:** dongle queue updates,
  availability checks, and releases are coordinated with the monitor condition
  mutex, so these operations cannot interleave while changing shared dongle
  state.
- **Cooldown:** a released dongle records its last-use time. Waiting coders use
  a timed condition-variable wait until the relevant cooldown can expire, and
  are also woken when dongle state or the simulation state changes.
- **Burnout detection:** a dedicated monitor thread checks coder deadlines and
  stops the simulation when it detects an expired deadline.
- **Interleaved output:** a shared print mutex protects log output so concurrent
  messages do not interleave.
- **Normal completion:** coder threads stop after reaching the required
  compilation count; the simulation also stops when the monitor detects a
  burnout.

## Thread synchronization mechanisms

- **`pthread_mutex_t` per dongle:** protects that dongle's `is_used`, cooldown
  timestamp, and request queue.
- **Monitor mutex:** protects the monitor stop flag and coder deadlines when
  they are read or updated.
- **Condition mutex and `pthread_cond_t`:** coordinate changes to dongle queues
  and let waiting coders sleep instead of continuously polling. Queue changes,
  dongle releases, and monitor shutdown broadcast to waiters. Cooldown waits
  use `pthread_cond_timedwait`.
- **Print mutex:** shared by coder and monitor threads to serialize log
  messages.

These locks provide thread-safe communication around shared state: for example,
the monitor changes the stop flag while holding the monitor mutex, and waiting
coders re-check that state before proceeding.

## Implementation notes

The request storage in the current implementation is a fixed-size, two-entry
ordered array per dongle. It applies FIFO or EDF ordering for the competing
requests it stores; it is not a general-purpose binary heap. For equal EDF
deadlines, the current comparison preserves insertion order, which can depend
on thread scheduling and is not a deterministic tie-break rule.

The subject specifies a single dongle when there is only one coder. In the
current implementation, acquisition is rejected when a coder's two dongle
references identify the same dongle, so the one-coder case does not complete a
compilation. These details should be addressed before claiming full compliance
with those subject requirements.

The parser reports a zero coder count as invalid, but that error is not
propagated back to `main`; use a positive number of coders.

## Resources

- The project subject: [`subject.md`](./subject.md).
- POSIX threads reference: [The Open Group Base Specifications — pthreads](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html).
- Linux manual pages: [`pthreads(7)`](https://man7.org/linux/man-pages/man7/pthreads.7.html),
  [`pthread_cond_wait(3)`](https://man7.org/linux/man-pages/man3/pthread_cond_wait.3.html),
  and [`pthread_mutex_lock(3)`](https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3.html).
- `gettimeofday(2)` and `usleep(3)` manual pages for the time measurement and
  waiting APIs used by the program.

### AI usage

AI assistance was used to help review the project against its subject, split
overlong functions into smaller helpers, inspect initialization and cleanup
paths, prepare the Makefile, and draft this README. The assistance concerned
the C implementation and project documentation; the resulting code and claims
should be checked and understood by the project author.
