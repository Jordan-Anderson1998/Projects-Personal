import time

"""
Problems Using Closures
Closures let you encapsulate behavior with persistent state. These problems will help you master that.
1. Rate Limiter
- Task: Write a function rate_limiter(n) that returns another function which allows only n calls per minute.
- Challenge: Use closures to store timestamps and enforce limits.

2. Custom Counter Generator
- Task: Create a function make_counter(start=0) that returns a function which increments and returns the count each time it's called.
- Bonus: Add optional reset and decrement functionality.

3. Memoization Decorator
- Task: Build a decorator using closures that caches the results of expensive function calls.
- Challenge: Handle functions with multiple arguments and keyword arguments.

4. Logger with Context
- Task: Create a function make_logger(prefix) that returns a logging function which prepends the prefix to every message.
- Bonus: Add timestamping and log level filtering.

5. Access Control Wrapper
- Task: Write a closure-based decorator that restricts access to a function unless a correct password is provided.
- Challenge: Store the password securely and allow limited retries.

"""


def rate_limiter(n: int, seconds: int) -> any:
    """
    :param n: Number of times to call the function is seconds
    :param seconds: Number of seconds to execute the function
    :return: Function(spam)
    """
    num_of_executions_per_seconds = seconds / n

    def spam():

        nonlocal n, seconds, num_of_executions_per_seconds
        total_executions = n
        num_of_executions = 1

        while total_executions > 0:

            print(f'SPAM Number: {num_of_executions} ')
            time.sleep(num_of_executions_per_seconds)
            total_executions -= 1
            num_of_executions += 1

    return spam()

if __name__ == '__main__':

    rate_limiter(10, 10)
    rate_limiter(100, 10)