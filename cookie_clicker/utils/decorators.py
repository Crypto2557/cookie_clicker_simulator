from typing import Callable


def register_strategy(skip: bool = False) -> Callable:
    """Registers a function as strategy.

    You can defined, whether this strategy should be skipped
    in default execution.

    Passing --all_strategies/-a command line argument will
    force to execute the skipped strategies.
    """
    from cookie_clicker import strategies

    def wrapper(func: Callable) -> Callable:

        strategies.all_strategies.append(func)
        if not skip:
            strategies.active.append(func)

        return func

    return wrapper


def register_competition(skip: bool = False, duration: float = 1e10, bigger_is_better: bool = True) -> Callable:
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
