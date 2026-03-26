from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор, который логирует начало и конец выполнения функции, ее результаты или возникшие ошибки.
    Должен принимать необязательный аргумент 'filename', который определяет,
    куда будут записываться логи (в файл или в консоль)
    """

    def my_decorator(func: Callable[..., Any]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"Function: {func.__name__} ok. Result: {result}\n")
                else:
                    print(f"Function: {func.__name__} ok. Result: {result}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"Function: {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"Function: {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return my_decorator
