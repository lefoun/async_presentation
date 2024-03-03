def say_hi():
    print("Hi!")


def add_int(left: int, right: int) -> int:
    return left + right


if __name__ == "__main__":
    say_hi() # defer
    x = 3
    y = 4
    ret = add_int(x, y)
    print(f"Result is {ret}")
