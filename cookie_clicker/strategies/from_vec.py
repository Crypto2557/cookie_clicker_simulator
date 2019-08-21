import copy
from typing import Optional, Dict
from decimal import Decimal
D = Decimal

from cookie_clicker.strategies.base import BaseStrategy
from cookie_clicker.buildings.factory import BuildingFactory


class StrategyFromVec(BaseStrategy):
    __default_dic = {
        "Cursor": 127,
        "Grandma": 128,
        "Farm": 128,
        "Mine": 128,
        "Factory": 128,
        "Bank": 128,
        "Temple": 128,
        "Wizard Tower": 128,
        "Shipment": 128,
        "Alchemy Lab": 64,
        "Portal": 32,
        "Time Machine": 16,
        "Antimatter Condenser": 8,
        "Prism": 4,
        "Chancemaker": 2,
        "Fractal Engine": 1
    }

    def __init__(self,
                 dic: Optional[Dict[str, int]] = None,
                 name: str = "irgendwas") -> None:
        super(StrategyFromVec, self).__init__(name=name)
        self.init_dic = dic or StrategyFromVec.__default_dic
        self.reset()

    def __call__(self, cookies: Decimal, cps: Decimal, time_left: Decimal,
                 factory: BuildingFactory) -> Optional[str]:

        def payback_period(cost: Decimal, cookies_in_bank: Decimal,
                           cps: Decimal, cps_building: Decimal) -> Decimal:
            return D(str(max(cost - cookies_in_bank / cps,
                             0))) / cps + cost / cps_building

        if cps == 0.0:
            return 'Cursor'

        payback_period_per_item = []

        for building_name in factory:
            building = factory[building_name]
            payback_period_per_item.append(
                (building_name,
                 payback_period(cost=building.cost,
                                cookies_in_bank=cookies,
                                cps=cps,
                                cps_building=building.cps)))

        payback_period_per_item.sort(key=lambda tup: tup[1])
        for best_option, *others in payback_period_per_item:
            if self.dic[best_option] > 0:
                self.dic[best_option] -= 1
                return best_option
        return None

    def reset(self) -> None:
        self.dic = copy.deepcopy(self.init_dic)
