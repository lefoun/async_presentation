from typing import Generator


def augment(a: int) -> Generator[int, None, None]:
    yield (a * 2)


def augemented_fib_sequence(max: int): 
    a = b = 1
    while a < max:
        augment(a)  # Does this yield ??
        a, b = b, a + b
    return 1










# Example 2

def augment2(a: int) -> Generator[int, None, None]:
    yield (a * 2)


def augemented_fib_sequence2(max: int) -> Generator[int, None, None]: # Generator[YieldType, SendType, ReturnType]
    a = b = 1
    while a < max:
        yield augment2(a)  # This yields because 
        a, b = b, a + b

