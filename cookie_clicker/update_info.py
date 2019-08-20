from __future__ import annotations
from typing import Dict, List


class UpdateInfo:
    """Class to track upgrade information."""

    def __init__(self,
                 update_info: Dict[str, Dict[str, float]] = None) -> None:
        self._build_growth = growth_factor
        self._info = update_info or {
          "Plain cookies": {'condition': {'total_cookies_generated': 5e4}, 'multipliers': 0.01, 'cost': 999999},
          "Sugar cookies": {'condition': {'total_cookies_generated': 2.5e5}, 'multipliers': 0.01, 'cost': 5e6},
          "Oatmeal raisin cookies": {'condition': {'total_cookies_generated': 5e5}, 'multipliers': 0.01, 'cost': 1e7},
          "Peanut butter cookies": {'condition': {'total_cookies_generated': 2.5e6}, 'multipliers': 0.01, 'cost': 5e7},
          "Coconut cookies": {'condition': {'total_cookies_generated': 5e6}, 'multipliers': 0.02, 'cost': 1e8},
          "Almond cookies": {'condition': {'total_cookies_generated': 5e6}, 'multipliers': 0.02, 'cost': 1e8},
          "Hazelnut cookies": {'condition': {'total_cookies_generated': 5e6}, 'multipliers': 0.02, 'cost': 1e8},
          "Walnut cookies": {'condition': {'total_cookies_generated': 5e6}, 'multipliers': 0.02, 'cost': 1e8},
          "White chocolate cookies": {'condition': {'total_cookies_generated': 2.5e7}, 'multipliers': 0.02, 'cost': 5e8},
          "Macadamia nut cookies": {'condition': {'total_cookies_generated': 5e7}, 'multipliers': 0.02, 'cost': 1e9},
          "Double-chip cookies": {'condition': {'total_cookies_generated': 2.5e8}, 'multipliers': 0.02, 'cost': 5e9},
          "White chocolate macadamia nut cookies": {'condition': {'total_cookies_generated': 5e8}, 'multipliers': 0.02, 'cost': 1e10},
          "All-chocolate cookies": {'condition': {'total_cookies_generated': 2.5e9}, 'multipliers': 0.02, 'cost': 5e10},
          "Dark chocolate-coated cookies": {'condition': {'total_cookies_generated': 5e9}, 'multipliers': 0.04, 'cost': 1e11},
          "White chocolate-coated cookies": {'condition': {'total_cookies_generated': 5e9}, 'multipliers': 0.04, 'cost': 1e11},
          "Eclipse cookies": {'condition': {'total_cookies_generated': 2.5e10}, 'multipliers': 0.02, 'cost': 5e11},
          "Zebra cookies": {'condition': {'total_cookies_generated': 5e10}, 'multipliers': 0.02, 'cost': 1e12},
          "Snickerdoodles": {'condition': {'total_cookies_generated': 2.5e11}, 'multipliers': 0.02, 'cost': 5e12},
          "Stroopwafels": {'condition': {'total_cookies_generated': 5e11}, 'multipliers': 0.02, 'cost': 1e13},
          "Macaroons": {'condition': {'total_cookies_generated': 2.5e12}, 'multipliers': 0.02, 'cost': 5e13},
          "Madeleines": {'condition': {'total_cookies_generated': 2.5e13}, 'multipliers': 0.02, 'cost': 5e14},
          "Palmiers": {'condition': {'total_cookies_generated': 2.5e13}, 'multipliers': 0.02, 'cost': 5e14},
          "Palets": {'condition': {'total_cookies_generated': 5e13}, 'multipliers': 0.02, 'cost': 1e15},
          "Sablés": {'condition': {'total_cookies_generated': 5e13}, 'multipliers': 0.02, 'cost': 1e15},
          "Gingerbread men": {'condition': {'total_cookies_generated': 5e14}, 'multipliers': 0.02, 'cost': 1e16},
          "Gingerbread trees": {'condition': {'total_cookies_generated': 5e14}, 'multipliers': 0.02, 'cost': 1e16},
          "Pure black chocolate cookies": {'condition': {'total_cookies_generated': 2.5e15}, 'multipliers': 0.04, 'cost': 5e16},
          "Pure white chocolate cookies": {'condition': {'total_cookies_generated': 2.5e15}, 'multipliers': 0.04, 'cost': 5e16},
          "Ladyfingers": {'condition': {'total_cookies_generated': 5e15}, 'multipliers': 0.03, 'cost': 1e17},
          "Tuiles": {'condition': {'total_cookies_generated': 2.5e16}, 'multipliers': 0.03, 'cost': 5e17},
          "Chocolate-stuffed biscuits": {'condition': {'total_cookies_generated': 5e16}, 'multipliers': 0.03, 'cost': 1e18},
          "Checker cookies": {'condition': {'total_cookies_generated': 2.5e17}, 'multipliers': 0.03, 'cost': 5e18},
          "Butter cookies": {'condition': {'total_cookies_generated': 5e17}, 'multipliers': 0.03, 'cost': 1e19},
          "Cream cookies": {'condition': {'total_cookies_generated': 2.5e18}, 'multipliers': 0.03, 'cost': 5e19},
          "Gingersnaps": {'condition': {'total_cookies_generated': 5e18}, 'multipliers': 0.04, 'cost': 1e20},
          "Cinnamon cookies": {'condition': {'total_cookies_generated': 2.5e19}, 'multipliers': 0.04, 'cost': 5e20},
          "Vanity cookies": {'condition': {'total_cookies_generated': 5e19}, 'multipliers': 0.04, 'cost': 1e21},
          "Cigars": {'condition': {'total_cookies_generated': 2.5e20}, 'multipliers': 0.04, 'cost': 5e21},
          "Pinwheel cookies": {'condition': {'total_cookies_generated': 5e20}, 'multipliers': 0.04, 'cost': 1e22},
        }

    def ugprade_items(self) -> List[str]:
        """Gets a list of buildable items."""
        return list(self._info.keys())

    def get_cost(self, item: str) -> float:
        """Gets the current cost of an item."""
        return self._info[item]['cost']

    def get_multipliers(self, item: str) -> float:
        """Gets the current CPS of an item."""
        return self._info[item]['multipliers']

    # ???
    def update_item(self, item: str) -> None:
        """Updates the cost of an item by the growth factor."""
        cost, cps = self._info[item].values()
        self._info[item] = {'cost': cost * self._build_growth, 'cps': cps}

    def clone(self) -> UpgradeInfo:
        """Returns a clone of this BuildInfo."""
        return UpgradeInfo(self._info)
