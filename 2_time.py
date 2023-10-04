import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} took {duration:.10f} seconds to execute.")
        return result
    return wrapper

# Example usage of the decorator
@measure_time
def function():
    time.sleep(2)

function()