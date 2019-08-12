from __future__ import annotations
from typing import Dict, List


class BuildingInfo:
    """Class to track build information."""

    def __init__(self,
                 building_info: Dict[str, Dict[str, float]] = None,
                 growth_factor: float = 1.15) -> None:
        self._build_growth = growth_factor
        self._buildings = building_info or {
            "Cursor": {
                'cost': 1.5e01,
                'cps': 0.1e00
            },
            "Grandma": {
                'cost': 1.0e02,
                'cps': 0.5e00
            },
            "Farm": {
                'cost': 1.1e03,
                'cps': 8.0e00
            },
            "Mine": {
                'cost': 1.2e04,
                'cps': 4.7e01
            },
            "Factory": {
                'cost': 1.3e05,
                'cps': 2.6e02
            },
            "Bank": {
                'cost': 1.4e06,
                'cps': 1.4e03
            },
            "Temple": {
                'cost': 2.0e07,
                'cps': 7.8e03
            },
            "Wizard Tower": {
                'cost': 3.3e08,
                'cps': 4.4e04
            },
            "Shipment": {
                'cost': 5.1e09,
                'cps': 2.6e05
            },
            "Alchemy Lab": {
                'cost': 7.5e10,
                'cps': 1.6e06
            },
            "Portal": {
                'cost': 1.0e12,
                'cps': 1.0e07
            },
            "Time Machine": {
                'cost': 1.4e13,
                'cps': 6.5e07
            },
            "Antimatter Condenser": {
                'cost': 1.7e14,
                'cps': 4.3e08
            },
            "Prism": {
                'cost': 2.1e15,
                'cps': 2.9e09
            },
            "Chancemaker": {
                'cost': 2.6e16,
                'cps': 2.1e10
            },
            "Fractal Engine": {
                'cost': 3.1e17,
                'cps': 1.5e11
            },
        }

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
        self._buildings[building] = {
            'cost': cost * self._build_growth,
            'cps': cps
        }

    def clone(self) -> BuildingInfo:
        """Returns a clone of this BuildInfo."""
        return BuildingInfo(self._buildings, self._build_growth)
