import abc

from typing import Any, List

class Registry(abc.ABC):
    _strategies: List = []
    _competitions: List = []

    @classmethod
    def register_strategy(cls, strategy) -> None:
        cls._strategies.append(strategy)

    @classmethod
    def strategies(cls, active_only: bool = True) -> List:
        if active_only:
            return [strat for strat in cls._strategies if not strat.skip]
        else:
            return cls._strategies

    @classmethod
    def get_strategies(cls, name: str) -> List:
        return [strat for strat in cls._strategies if name in strat.name]


    @classmethod
    def register_competition(cls, competition) -> None:
        cls._competitions.append(competition)
