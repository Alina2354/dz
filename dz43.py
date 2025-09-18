import time
import random
from functools import wraps

def retry(times=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed. Retrying in {delay} seconds...")
                    time.sleep(delay)
            else:
                raise last_exception

        return wrapper
    return decorator


@retry(times=3, delay=1)
def unstable():
    if random.random() < 0.7:
        raise ValueError("fail")
    return "ok"

if __name__ == '__main__':
    try:
        result = unstable()
        print(f"Function returned: {result}")
    except ValueError as e:
        print(f"Function failed after multiple retries: {e}")

