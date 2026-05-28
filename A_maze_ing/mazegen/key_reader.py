import sys
import termios
import tty


def read_key() -> str:
    """Read a single keypress from stdin in raw mode.

    Temporarily sets the terminal to raw mode so that each key is returned
    immediately without waiting for Enter. Terminal settings are restored
    via a finally block.

    Returns:
        The single character string corresponding to the key pressed.
    """
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch
