""""""
from __future__ import annotations
import copy
import math
from typing import List, Union, Dict
from dataclasses import dataclass, field
from decimal import Decimal

from cookie_clicker.utils import Config
# from cookie_clicker.clicker_state import ClickerState

D = Decimal


class BuildingFactory:
    """"""

    def __init__(self,
                 building_info: Union[str, Dict[str, Dict[str, float]]],
                 growth_factor: Decimal = Config.Defaults.GROWTH_FACTOR
                ) -> None:
        super(BuildingFactory, self).__init__()

        self._built_buildings: Dict[str, Building] = {}
        self.growth_factor = D(str(growth_factor))
        # self.state = ClickerState()

        if isinstance(building_info, str):
            self._buildings = Config.load(building_info)

        elif isinstance(building_info, dict):
            self._buildings = copy.deepcopy(building_info)

        else:
            raise ValueError(
                f'Not supported build info type: {type(building_info)}')

    @property
    def buildings(self) -> List[str]:
        """"""
        return list(self._buildings.keys())

    def __getitem__(self, building_name: str) -> Building:
        """"""
        if building_name not in self._built_buildings:
            _info = self._buildings[building_name]

            self._built_buildings[building_name] = Building(
                factory=self,
                name=building_name,
                initial_cost=D(str(_info["cost"])),
                initial_cps=D(str(_info["cps"])),
                count=0)

        return self._built_buildings[building_name]

    def __iter__(self):
        """"""
        return iter(self.buildings)


@dataclass
class Building:
    """"""
    name: str
    initial_cost: Decimal
    initial_cps: Decimal
    factory: BuildingFactory = field(repr=False)
    count: int = 0

    @property
    def cost(self) -> Decimal:
        """ computes the costs based on the growth_factor, amount of
        buildings already built and the initial cost of the building """
        cost = self.initial_cost * self.factory.growth_factor**self.count
        return D(math.ceil(cost))

    @property
    def cps(self) -> Decimal:
        """ currently only returns the initial_cps, since upgrades
        are not implemented yet """
        return self.initial_cps
