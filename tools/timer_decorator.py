from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result

    return wrapper
