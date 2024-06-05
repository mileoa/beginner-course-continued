from typing import Callable

def disable(func: Callable) -> Callable:
    def wrapper() -> None:
        pass
    return wrapper

def use_itself(func: Callable) -> Callable:
    def wrapper(*args: int) -> Callable:
        return func(func(*args))
    return wrapper

@disable
def delete_db() -> None:
    print("Всё подчистили.")

@use_itself
def inc(a: int) -> int:
    return a + 1

delete_db()
print(inc(1))