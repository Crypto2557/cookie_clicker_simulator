from cookie_clicker.utils.decorators import register_strategy

import copy

class StrategiefromVec:
    __name__ = 'irgendwas'

    __default_dic = {
            "Cursor"                : 127,
            "Grandma"               : 128,
            "Farm"                  : 128,
            "Mine"                  : 128,
            "Factory"               : 128,
            "Bank"                  : 128,
            "Temple"                : 128,
            "Wizard Tower"          : 128,
            "Shipment"              : 128,
            "Alchemy Lab"           : 64,
            "Portal"                : 32,
            "Time Machine"          : 16,
            "Antimatter Condenser"  : 8,
            "Prism"                 : 4,
            "Chancemaker"           : 2,
            "Fractal Engine"        : 1
            }

    def __init__(self, dic=None):

        self.init_dic = dic or StrategiefromVec.__default_dic
        self.reset()


    def __call__(self, cookies, cps, time_left, factory):
        def payback_period(cost: float, cookies_in_bank: float, cps: float,
                                 cps_building: float) -> float:
            return max(cost - cookies / cps, 0) / cps + cost / cps_building

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

    def reset(self):
        self.dic = copy.deepcopy(self.init_dic)



register_strategy(skip=False)(StrategiefromVec({

    "Cursor"                : 145-1,
    "Grandma"               : 128,
    "Farm"                  : 128,
    "Mine"                  : 128,
    "Factory"               : 128,
    "Bank"                  : 128,
    "Temple"                : 128,
    "Wizard Tower"          : 128,
    "Shipment"              : 128,
    "Alchemy Lab"           : 64,
    "Portal"                : 44,
    "Time Machine"          : 31,
    "Antimatter Condenser"  : 18,
    "Prism"                 : 12,
    "Chancemaker"           : 8,
    "Fractal Engine"        : 3
}))
