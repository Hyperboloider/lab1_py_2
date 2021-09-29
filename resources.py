import time
from typing import Callable
from functools import wraps

class Timer:


    @staticmethod
    def timeit(method: Callable):
        @wraps(method)
        def timed(*args):
            time_start = time.time()
            result = method(*args)
            time_end = time.time()

            print("time:", round(time_end - time_start, 3))
            return result
        
        return timed