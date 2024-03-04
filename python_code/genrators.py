def fib_sequence(max: int):
    a = b = 1
    while a < max:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    pass