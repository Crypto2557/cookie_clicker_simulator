""" Shopping List strategy """
from pathlib import Path
from os.path import basename
from decimal import Decimal
from typing import List, Callable, Union, Optional

from cookie_clicker.utils import Config
from cookie_clicker.strategies.base import BaseStrategy
from cookie_clicker.buildings import BuildingFactory


class ShoppingListStrategy(BaseStrategy):

    @classmethod
    def load(cls, shopping_list_path: str) -> List[str]:
        with open(shopping_list_path) as shopping_list:
            purchases = [str(x).strip() for x in shopping_list]
        return purchases

    @classmethod
    def save(cls, shopping_list_path: str, purchases: List[str]) -> None:
        with open(shopping_list_path, 'w') as shopping_list:
            shopping_list.write('\n'.join(purchases) + '\n')

    def __init__(self, shopping_list_path: str) -> None:
        name = basename(shopping_list_path)
        super(ShoppingListStrategy, self).__init__(name=name)

        self.purchases = ShoppingListStrategy.load(shopping_list_path)
        self.purchases_current: List[str] = []

    def __call__(self, cookies: Decimal, cps: Decimal, time_left: Decimal,
                 factory: BuildingFactory) -> Optional[str]:

        if cookies == 15 and cps == 0:
            self.purchases_current = self.purchases.copy()

        if len(self.purchases_current) > 0:
            purchase = self.purchases_current.pop(0)
            if purchase == 'None':
                return None
            else:
                return purchase
        else:
            return None

    @classmethod
    def create_from_folder(cls,
                           folder: str = Config.Defaults.SHOPPING_LISTS_FOLDER
                          ) -> None:
        for item in sorted(Path(folder).iterdir()):
            ShoppingListStrategy(str(item))
