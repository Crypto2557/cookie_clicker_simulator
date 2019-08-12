from __future__ import annotations
from typing import Dict, List, Union

import copy

from cookie_clicker.utils import read_config_file


class BuildingInfo:
    """Class to track build information."""

    def __init__(self,
                 building_info: Union[str, Dict[str, Dict[str, float]]],
                 growth_factor: float = 1.15) -> None:
        self._build_growth = growth_factor

        if isinstance(building_info,  str):
            self._buildings = read_config_file(building_info)

        elif isinstance(building_info, dict):
            self._buildings = copy.deepcopy(building_info)

        else:
            raise ValueError(f'Not supported build info type: {type(building_info)}')

    @property
    def buildings(self) -> List[str]:
        return list(self._buildings.keys())

    def get_cost(self, building: str) -> float:
        """Gets the current cost of an building."""
        return self._buildings[building]['cost']

    def get_cps(self, building: str) -> float:
        """Gets the current CPS of an building."""
        return self._buildings[building]['cps']

    def update_building(self, building: str) -> None:
        """Updates the cost of an building by the growth factor."""
        cost, cps = self._buildings[building].values()
        self._buildings[building]["cost"] *= self._build_growth

    def clone(self) -> BuildingInfo:
        """Returns a clone of this BuildInfo."""
        return BuildingInfo(self._buildings, self._build_growth)
