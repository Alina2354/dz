from functools import wraps

def cache(func):
    cached_results = {}

    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"Возвращение результата из кэша для {args}")
            return cached_results[args]
        else:
            result = func(*args)
            cached_results[args] = result
            print(f"Вычисление {func.__name__}{args}")
            return result

    return wrapper


@cache
def slow_add(a, b):
    print(f"Вычисление {a} + {b}")
    return a + b


if __name__ == '__main__':
    print(slow_add(2, 3))
    print(slow_add(2, 3))  

