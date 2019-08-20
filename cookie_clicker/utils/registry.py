import abc

from typing import Any, List, Dict

from collections import OrderedDict

class Registry(abc.ABC):
    _strategies: OrderedDict = OrderedDict()
    _competitions: OrderedDict = OrderedDict()

    @classmethod
    def register_strategy(cls, strategy) -> None:
        cls._strategies[strategy.name] = strategy

    @classmethod
    def strategies(cls, active_only: bool = True) -> List:
        if active_only:
            return [strat for strat in cls._strategies.values() if not strat.skip]
        else:
            return list(cls._strategies.values())

    @classmethod
    def get_strategies(cls, name: str) -> List:
        return [strat for strat in cls._strategies.values() if name in strat.name]

    @classmethod
    def get_strategy(cls, name: str):
        return cls._strategies[name]


    @classmethod
    def register_competition(cls, competition) -> None:
        """Registers a function as competition.

        You can define whether this competition should be skipped
        in default execution.

        Passing --all_competitions/-c command line argument will
        force to execute the skipped strategies.
        """
        cls._competitions[competition.name] = competition

    @classmethod
    def competitions(cls, active_only: bool = True) -> List:
        if active_only:
            return [comp for comp in cls._competitions.values() if not comp.skip]
        else:
            return list(cls._competitions.values())


    @classmethod
    def get_competition(cls, name: str):
        return cls._competitions[name]
