# import time 

# def my_fucntion():
#     """A simple function that takes some time."""
#     print("Starting my_function ...")
#     time.sleep(1)  # Simulate some work
#     print("my_function finish")


# my_fucntion()



import time

def timer_decorator(func):
    """A decorator to measure the execution time of a function."""
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds.")
    return wrapper


@timer_decorator
def my_function_with_timer():
    """A simple function with a timer."""
    print("Starting my_function_with_timer...")
    time.sleep(1)
    print("my_function_with_timer finished.")

my_function_with_timer()