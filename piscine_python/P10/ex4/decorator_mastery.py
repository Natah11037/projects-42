from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}")
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
            if not kwargs:
                raise SyntaxError("Please enter a key: value")
            power = kwargs.get("power", 0)
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return power
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass
    
    @power_validator
    def cast_spell(self, spell_name: str, power: int) -> str:
        try:
            return f"Succesfully cast {spell_name} with {power} power"
        except SyntaxError as e:
            return e


def main():
    print("\nTesting spell timer...")
    print(fireball())

    print("\nTesting to cast a spell...")
    arthur = MageGuild()
    print(arthur.cast_spell("zoubidoulala", 15))


if __name__ == "__main__":
    main()
