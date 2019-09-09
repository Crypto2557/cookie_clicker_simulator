""""""
from __future__ import annotations
from typing import Union, Dict
from decimal import Decimal
from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.buildings import BuildingFactory
from cookie_clicker.strategies.base import BaseStrategy

D = Decimal


class Simulator:
    """ Simulates a Cookie Clicker game.
    Calculates the outcome of a game given a
    duration and a strategy.
    """

    def __init__(self,
                 building_info: Union[str, Dict[str, Dict[str, float]]],
                 duration: Decimal = D(1e10)) -> None:

        self.building_info = building_info
        self.duration = D(duration)
        self.state = self.new_state()

    def new_state(self) -> ClickerState:
        """ Creates a new state object from given building info """
        return ClickerState.new(self.building_info)

    @property
    def factory(self) -> BuildingFactory:
        """ Getter for state's building factory"""
        return self.state.factory

    def reset(self, strategy: BaseStrategy) -> None:
        """ Creates a new state object and resets the strategy"""
        self.state = self.new_state()
        strategy.reset()

    @property
    def ready(self) -> bool:
        """ Checks, whether the state's current time is above the duration
        meaning, the simulation is ready. """
        return self.state.current_time > self.duration

    def run_strategy(self, strategy: BaseStrategy,
                     print_results: bool = True) -> ClickerState:
        """ Runs a simulation with one strategy. Following steps are done:
        - a new state is created
        - strategy is reset
        - until current time has not reached the duration
            * strategy is asked, which item should be bought
            * as long as the item is not None, state buys the item
            (meaning waiting until enough deposit is present)
        - finally state waits for the remaining amount of time
        - if "print_results" is set, print the state information
        """

        self.reset(strategy)

        while not self.ready:
            # Determine the item to buy next
            item_to_buy = strategy(self.state, self.duration)

            if item_to_buy is None:
                break

            self.state.buy(item_to_buy)

        time_remain = self.duration - self.state.current_time
        self.state.wait(time_remain)

        if print_results:
            print(self.state)

        return self.state
