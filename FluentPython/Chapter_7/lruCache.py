from clock import clock
import functools


@clock
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci_1(n - 2) + fibonacci_1(n - 1)


@functools.lru_cache()
@clock
def fibonacci_2(n):
    if n < 2:
        return n
    return fibonacci_2(n - 2) + fibonacci_2(n - 1)


if __name__ == "__main__":
    print(fibonacci_1(30))
    print('*' * 50)
    print(fibonacci_2(30))
