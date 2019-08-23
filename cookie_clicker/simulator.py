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
        """"""
        return ClickerState.new(self.building_info)

    @property
    def factory(self) -> BuildingFactory:
        """"""
        return self.state.factory

    def reset(self, strategy: BaseStrategy) -> None:
        """"""
        self.state = self.new_state()
        strategy.reset()

    @property
    def ready(self) -> bool:
        """"""
        return self.state.current_time > self.duration

    def run_strategy(self, strategy: BaseStrategy,
                     print_results: bool = True) -> ClickerState:
        """Runs a simulation with one strategy."""

        self.reset(strategy)

        while not self.ready:
            item_to_buy = strategy(
                self.state.current_cookies, self.state.cps,
                self.duration - self.state.current_time,
                self.factory)  # Determine the item to buy next

            if item_to_buy is None:
                break

            self.state.buy(item_to_buy)

        time_remain = self.duration - self.state.current_time
        self.state.wait(time_remain)

        if print_results:
            print(self.state)

        return self.state
