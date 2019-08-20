from tabulate import tabulate
from typing import Callable, List, Type, Tuple, Union, Dict
from decimal import Decimal

D = Decimal

from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.buildings import BuildingFactory
from cookie_clicker.utils import Registry
from cookie_clicker.strategies.base import BaseStrategy


class Simulator:
    """ Simulates a Cookie Clicker game.
    Calculates the outcome of a game given a
    duration and a strategy.
    """

    def __init__(self, building_info: Union[str, Dict[str, Dict[str, float]]],
                 duration: Decimal = D(1e10)) -> None:

        self.building_info = building_info
        self.duration = D(duration)

    def new_factory(self):
        return BuildingFactory(self.building_info)

    @property
    def state(self):
        return self.factory.state

    def reset(self, strategy: BaseStrategy):
        self.factory = self.new_factory()
        strategy.reset()

    @property
    def ready(self):
        return self.state.current_time > self.duration

    def run_strategy(self, strategy: BaseStrategy, print_results: bool = True) -> ClickerState:
        """Runs a simulation with one strategy."""

        self.reset(strategy)

        while not self.ready:
            item_to_buy = strategy(
                self.state.current_cookies,
                self.state.cps,
                self.duration - self.state.current_time,
                self.factory)  # Determine the item to buy next

            if item_to_buy is None:
                break

            self.factory.build(item_to_buy)

        time_remain = self.duration - self.state.current_time
        self.state.wait(time_remain)

        if print_results:
            print(self.state)

        return self.state

    def run_strategies(self, strategy: str = None, run_all: bool = False, print_results: bool = False) -> List[Tuple[str, ClickerState]]:
        clicker_states = []

        if strategy is not None:
            strategy_list = Registry.get_strategies(strategy)
        else:
            strategy_list = Registry.strategies(active_only=not run_all)

        for strat in strategy_list:
            clicker_states.append((strat.name, self.run_strategy(strat, print_results)))

        return clicker_states


    def print_comparison(self, clicker_states: List[Tuple[str, ClickerState]]) -> None:
        headers = ['#', 'Strategy', 'All Time', 'Current', 'CPS']
        tablerows = []
        for i, (name, clicker_state) in enumerate(clicker_states):
            tablerows.append([
                i,
                name,
                clicker_state.total_cookies,
                clicker_state.current_cookies,
                clicker_state.cps
            ])
        table = tabulate(tablerows,
                         headers,
                         tablefmt='fancy_grid',
                         numalign='center')
        print(table)
