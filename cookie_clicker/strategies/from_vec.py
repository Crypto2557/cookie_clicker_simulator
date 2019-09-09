""""""
import copy
from typing import Optional, Dict
from decimal import Decimal
from cookie_clicker.strategies.impl import MonsterStrategy
from cookie_clicker.clicker_state import ClickerState

D = Decimal


class StrategyFromVec(MonsterStrategy):
    """
    """
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

    def __call__(self, state: ClickerState, duration: Decimal) -> Optional[str]:

        if state.cps == 0.0:
            return 'Cursor'

        payback_period_per_item = self.calculate_pp_per_item(state)

        for best_option, _ in payback_period_per_item:
            if self.dic[best_option] > 0:
                self.dic[best_option] -= 1
                return best_option

        return None

    def reset(self) -> None:
        self.dic = copy.deepcopy(self.init_dic)
