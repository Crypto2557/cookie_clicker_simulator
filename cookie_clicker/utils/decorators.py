from typing import Callable
from decimal import Decimal

D = Decimal

def register_competition(skip: bool = False, duration: Decimal = D(1e10), bigger_is_better: bool = True) -> Callable:
    """Registers a function as competition.

    You can define whether this competition should be skipped
    in default execution.

    Passing --all_competitions/-c command line argument will
    force to execute the skipped strategies.
    """

    from cookie_clicker import competitions

    def wrapper(func: Callable) -> Callable:

        competitions.all_competitions.append((func, duration, bigger_is_better))
        if not skip:
            competitions.active.append((func, duration, bigger_is_better))

        return func

    return wrapper
