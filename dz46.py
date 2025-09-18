import signal
import time
from functools import wraps

class TimeoutError(Exception):
    pass

def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def timeout_handler(signum, frame):
                raise TimeoutError(f"Function {func.__name__} timed out after {seconds} seconds")

            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)

            return result

        return wrapper
    return decorator


if __name__ == '__main__':
    @timeout(seconds=2)
    def long_task():
        print("Начало выполнения долгой задачи...")
        time.sleep(3)  
        print("Долгая задача завершена!")
        return "Долгая задача выполнена успешно"

    try:
        result = long_task()
        print(result)
    except TimeoutError as e:
        print(f"Ошибка: {e}")
