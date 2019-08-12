from typing import Callable

from cookie_clicker import strategies

def register_strategy(skip: bool = False) -> Callable:
    """Registers a function as strategy.

    You can defined, whether this strategy should be skipped
    in default execution.

    Passing --all_strategies/-a command line argument will
    force to execute the skipped strategies.
    """

    def wrapper(func: Callable) -> Callable:

        strategies.all_strategies.append(func)
        if not skip:
            strategies.active.append(func)

        return func

    return wrapper
