from collections.abc import Callable
from functools import wraps
import time


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable):
        @wraps(func)
        def retry(*args, **kwargs):
            i = 1
            y = 1
            while i <= max_attempts and y <= max_attempts:
                try:
                    res = func(*args, **kwargs)
                    y = max_attempts
                    y += 1
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")
                    i += 1
            if i - 1 == max_attempts:
                return f"Spell casting failed after {max_attempts} attempts"
            else:
                return res
        return retry
    return decorator


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        total_time = end - start
        print(f"Spell completed in {total_time:.3f} seconds")
        return res
    return wrapper


@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable):
        @wraps(func)
        def power(*args, **kwargs):
            if "power" in kwargs:
                if kwargs["power"] < min_power:
                    return "Insufficient power for this spell"
            elif args:
                if isinstance(args[-1], int):
                    if args[-1] < min_power:
                        return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return power
    return decorator


@retry_spell(3)
def not_good_func():
    raise TypeError("msg")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if isinstance(power, int) and isinstance(spell_name, str):
            return f"Successfully cast '{spell_name}' with {power} power"
        raise TypeError("Error: please put a spell_name: "
                        "str variable and a power: int variable")


def main():
    print("Testing spell timer...")
    print(fireball())

    print("\nTesting retry spell...")
    print(not_good_func())

    print("\nTesting MageGuild...")
    arthur = MageGuild()
    print(arthur.validate_mage_name('Arthur'))
    print(arthur.validate_mage_name("$$xX_le_sasuke_du_68_Xx$$"))
    try:
        print(arthur.cast_spell("arthur", 67))
    except (SyntaxError, TypeError) as e:
        print(e)


if __name__ == "__main__":
    main()
