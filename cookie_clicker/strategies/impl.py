"""Here you find strategies, that are more comprehensive"""
from typing import Optional
from decimal import Decimal
from cookie_clicker.strategies.base import BaseStrategy
from cookie_clicker.buildings.factory import BuildingFactory

D = Decimal


class CheapStrategy(BaseStrategy):
    """This strategy buys always the cheapest item."""

    def __init__(self) -> None:
        super(CheapStrategy, self).__init__(name="cheap")

    def __call__(self, cookies: Decimal, cps: Decimal, time_left: Decimal,
                 factory: BuildingFactory) -> Optional[str]:
        costs = [(factory[building].cost, building) for building in factory]
        costs.sort(key=lambda tup: tup[0])

        if costs[0][0] <= (time_left * cps + cookies):
            return costs[0][1]

        return None


class ExpensiveStrategy(BaseStrategy):
    """This strategy buys always the most expensive item."""

    def __init__(self) -> None:
        super(ExpensiveStrategy, self).__init__(name="expensive")

    def __call__(self, cookies: Decimal, cps: Decimal, time_left: Decimal,
                 factory: BuildingFactory) -> Optional[str]:
        costs = [(factory[building].cost, building) for building in factory]
        costs.sort(key=lambda tup: tup[0], reverse=True)

        for cost, building in costs:
            if cost <= (time_left * cps + cookies):
                return building
        return None


class MonsterStrategy(BaseStrategy):
    """This strategy buys the item with the earliest payback"""

    def __init__(self, name: str = 'Monster'):
        super(MonsterStrategy, self).__init__(name=name)

    def __call__(self, cookies: Decimal, cps: Decimal, time_left: Decimal,
                 factory: BuildingFactory) -> Optional[str]:

        if cps == 0.0:
            return 'Cursor'

        payback_period_per_item = self.calculate_pp_per_item(factory=factory,
                                                             cookies=cookies,
                                                             cps=cps)

        best_option = payback_period_per_item[0][0]
        return best_option

    def calculate_pp_per_item(self, factory: BuildingFactory, cookies: Decimal,
                              cps: Decimal):
        """"""
        payback_period_per_item = []
        for building_name in factory:
            building = factory[building_name]
            payback_period_per_item.append(
                (building_name,
                 self.payback_period(cost=building.cost,
                                     cookies_in_bank=cookies,
                                     cps=cps,
                                     cps_building=building.cps)))

        payback_period_per_item.sort(key=lambda tup: tup[1])
        return payback_period_per_item

    @staticmethod
    def payback_period(cost: Decimal, cookies_in_bank: Decimal, cps: Decimal,
                       cps_building: Decimal) -> Decimal:
        """"""
        return D(str(max(cost - cookies_in_bank / cps,
                         0))) / cps + cost / cps_building
