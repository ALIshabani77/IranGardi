import time

def timer(func):
    """دکوراتور برای اندازه‌گیری زمان اجرا"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"زمان اجرا: {end - start:.2f} ثانیه")
        return result
    return wrapper