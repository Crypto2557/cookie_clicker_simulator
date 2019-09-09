""""""
import abc
from typing import List
from collections import OrderedDict


class Registry(abc.ABC):
    """ This class is responsible for registration and access
    of strategies and competitions """
    _strategies: OrderedDict = OrderedDict()
    _competitions: OrderedDict = OrderedDict()

    @classmethod
    def register_strategy(cls, strategy) -> None:
        """ Registers a strategy """
        cls._strategies[strategy.name] = strategy

    @classmethod
    def strategies(cls, active_only: bool = True) -> List:
        """ Returns a list of strategies. Optionally only
        active strategies may be selected. """
        if active_only:
            return [
                strat for strat in cls._strategies.values() if not strat.skip
            ]
        return list(cls._strategies.values())

    @classmethod
    def get_strategies(cls, name: str) -> List:
        """ Returns a list of strategies containing
        the passed name in their name. """

        return [
            strat for strat in cls._strategies.values() if name in strat.name
        ]

    @classmethod
    def get_strategy(cls, name: str):
        """ Returns a registered strategy with the given name. """
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
        """ Returns a list of competitions. Optionally only
        active competitions may be selected. """
        if active_only:
            return [
                comp for comp in cls._competitions.values() if not comp.skip
            ]
        return list(cls._competitions.values())

    @classmethod
    def get_competition(cls, name: str):
        """ Returns a registered competition with the given name. """
        return cls._competitions[name]
