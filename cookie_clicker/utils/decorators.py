from typing import Callable, List

from cookie_clicker.strategies import active, all_strategies

def register_strategy(skip=False):
    global active, all_strategies

    def wrapper(func: Callable):
        all_strategies.append(func)
        if not skip:
            active.append(func)
        return func

    return wrapper
