# Source: https://www.mybluelinux.com/pyhon-lru-cache-with-time-expiration/

from functools import lru_cache, wraps
from datetime import datetime, timedelta

def timed_lru_cache(seconds: int, maxsize: int = None):

    def wrapper_cache(func):
        # print('I will use lru_cache')
        func = lru_cache(maxsize=maxsize)(func)
        # print('I\'m setting func.lifetime')
        func.lifetime = timedelta(seconds=seconds)
        # print('I\'m setting func.expiration')
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            # print('Check func expiration')
            print(f'datetime.utcnow(): {datetime.utcnow()}, func.expiration: {func.expiration}')
            if datetime.utcnow() >= func.expiration:
                print('func.expiration lru_cache lifetime expired')
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache