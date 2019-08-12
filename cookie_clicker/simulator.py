from tabulate import tabulate
from typing import Callable, List

from cookie_clicker.building_info import BuildingInfo
from cookie_clicker.clicker_state import ClickerState


class Simulator:
    """ Simluates a Cookie Clicker game.
    Calculates the outcome of a game given a
    duration and a strategy.
    """

    def __init__(self, building_info: BuildingInfo,
                 duration: float = 1e10) -> None:

        self.building_info = building_info
        self.duration = duration

    def run_strategy(self, strategy: Callable) -> ClickerState:
        """Runs a simulation with one strategy."""
        clicker_state = ClickerState()
        building_info = self.building_info()

        while clicker_state.current_time <= self.duration:
            item_to_buy = strategy(
                clicker_state.current_cookies, clicker_state.cps,
                self.duration - clicker_state.current_time,
                building_info)  # Determine the item to buy next

            if item_to_buy is None:
                break

            elapsed = clicker_state.time_until(
                building_info.get_cost(item_to_buy)
            )  # Determine how much time must elapse until it is possible to purchase the item.

            if clicker_state.current_time + elapsed > self.duration:
                break

            clicker_state.wait(elapsed)

            clicker_state.buy_item(item_to_buy,
                                   building_info.get_cost(item_to_buy),
                                   building_info.get_cps(item_to_buy))

            building_info.update_building(item_to_buy)

        clicker_state.wait(self.duration - clicker_state.current_time)

        print(clicker_state)

        return clicker_state

    def run_strategies(self, strategies: List[Callable]) -> List[ClickerState]:
        clicker_states = []
        for strategy in strategies:
            clicker_states.append(self.run_strategy(strategy))
        return clicker_states

    def print_comparison(self, clicker_states):
        headers = ['Strategy', 'All Time', 'Current', 'CPS']
        tablerows = []
        for i, clicker_state in enumerate(clicker_states):
            tablerows.append([
                i,
                clicker_state.total_cookies,
                clicker_state.current_cookies,
                clicker_state.cps
            ])
        table = tabulate(tablerows,
                         headers,
                         tablefmt='fancy_grid',
                         numalign='center')
        print(table)
