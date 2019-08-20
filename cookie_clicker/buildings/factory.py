from __future__ import annotations

import copy
import math

from typing import Callable, List, Type, Tuple, Union, Dict
from dataclasses import dataclass, field

from cookie_clicker.utils import Config
from cookie_clicker.clicker_state import ClickerState

class BuildingFactory(object):

    def __init__(self, building_info: Union[str, Dict[str, Dict[str, float]]], growth_factor=1.15) -> None:
        super(BuildingFactory, self).__init__()

        self._built_buildings = {}
        self.growth_factor = growth_factor
        self.state = ClickerState()


        if isinstance(building_info,  str):
            self._buildings = Config.load(building_info)

        elif isinstance(building_info, dict):
            self._buildings = copy.deepcopy(building_info)

        else:
            raise ValueError(f'Not supported build info type: {type(building_info)}')

    @property
    def buildings(self) -> List[str]:
        return list(self._buildings.keys())

    def __getitem__(self, building_name: str) -> Building:

        if building_name not in self._built_buildings:
            _info = self._buildings[building_name]
            kwargs = dict(
                factory=self,
                name=building_name,
                initial_cost=_info["cost"],
                initial_cps=_info["cps"],
                count=0
            )
            self._built_buildings[building_name] = Building(**kwargs)

        return self._built_buildings[building_name]

    def build(self, building_name: str) -> Building:
        if building_name not in self._buildings:
            return None

        building = self[building_name]
        self.state.buy(building)

        building.count += 1
        return building

    def time_until(self, building_name: str) -> float:
        building = self[building_name]
        return self.state.time_until(building)

@dataclass
class Building:
    name: str
    initial_cost: float
    initial_cps: float
    count: int = 0
    factory: BuildingFactory = field(repr=False, default=None)

    @property
    def cost(self):
        return math.ceil(self.initial_cost * self.factory.growth_factor**self.count)

    @property
    def cps(self):
        return self.initial_cps

