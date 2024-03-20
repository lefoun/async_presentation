from typing import Generator


# Eager version
def fib_sequence_list(max: int) -> list[int]:
    a = b = 1
    lst = [a]
    while a < max:
        lst.append(a)
        a, b = b, a + b
    return lst


# Lazy version
def fib_sequence(max: int) -> Generator[int, None, None]: # Generator[YieldType, SendType, ReturnType]
    a = b = 1
    while a < max:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    eager_fibonnaci: list[int] = fib_sequence_list(10000) # a lot of compute
    lazy_fibonnaci: Generator[int, None, None] = fib_sequence(10000) # barely any compute
    for fib in lazy_fibonnaci:
        print(f"{fib}")