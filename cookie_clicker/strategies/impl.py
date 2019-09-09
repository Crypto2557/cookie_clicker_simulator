"""Here you find strategies, that are more comprehensive"""
from typing import Optional
from decimal import Decimal
from cookie_clicker.strategies.base import BaseStrategy
from cookie_clicker.buildings.factory import Building
from cookie_clicker.clicker_state import ClickerState

D = Decimal


class CheapStrategy(BaseStrategy):
    """This strategy buys always the cheapest item."""

    def __init__(self) -> None:
        super(CheapStrategy, self).__init__(name="cheap")

    def __call__(self, state: ClickerState, duration: Decimal) -> Optional[str]:
        factory = state.factory
        time_left = duration - state.current_time

        costs = [(factory[name].cost, name) for name in factory]
        costs.sort(key=lambda tup: tup[0])

        if costs[0][0] <= (time_left * state.cps + state.current_cookies):
            return costs[0][1]

        return None


class ExpensiveStrategy(BaseStrategy):
    """This strategy buys always the most expensive item."""

    def __init__(self) -> None:
        super(ExpensiveStrategy, self).__init__(name="expensive")

    def __call__(self, state: ClickerState, duration: Decimal) -> Optional[str]:
        factory = state.factory
        time_left = duration - state.current_time

        costs = [(factory[building].cost, building) for building in factory]
        costs.sort(key=lambda tup: tup[0], reverse=True)

        for cost, building in costs:
            if cost <= (time_left * state.cps + state.current_cookies):
                return building
        return None


class MonsterStrategy(BaseStrategy):
    """This strategy buys the item with the earliest payback"""

    def __init__(self, name: str = 'Monster'):
        super(MonsterStrategy, self).__init__(name=name)

    def __call__(self, state: ClickerState, duration: Decimal) -> Optional[str]:

        if state.cps == 0.0:
            return 'Cursor'

        payback_period_per_item = self.calculate_pp_per_item(state)

        best_option = payback_period_per_item[0][0]
        return best_option

    def calculate_pp_per_item(self, state: ClickerState):
        """"""
        payback_period_per_item = []
        for building_name in state.factory:
            building = state.factory[building_name]
            payback_period_per_item.append(
                (building_name,
                 self.payback_period(building=building, state=state)))

        payback_period_per_item.sort(key=lambda tup: tup[1])
        return payback_period_per_item

    @staticmethod
    def payback_period(building: Building, state: ClickerState) -> Decimal:
        """"""
        return D(str(max(building.cost - state.current_cookies / state.cps,
                         0))) / state.cps + building.cost / building.cps
