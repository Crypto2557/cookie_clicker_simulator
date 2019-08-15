""" Shopping List strategy """
import pathlib
from typing import List, Callable, Union
from cookie_clicker.utils.decorators import register_strategy


def load_purchases_file(shopping_list_path: str) -> List[str]:
    with open(shopping_list_path) as shopping_list:
        purchases = [str(x).strip() for x in shopping_list]

    return purchases


def save_purchases_file(shopping_list_path: str, purchases: List[str]) -> None:
    with open(shopping_list_path, 'w') as shopping_list:
        shopping_list.write('\n'.join(purchases) + '\n')


def get_shopping_list_strategy_from_file(shopping_list_path: str) -> Callable:
    return get_shopping_list_strategy_from_list(load_purchases_file(shopping_list_path))


def get_shopping_list_strategy_from_list(purchases: List[str]) -> Callable:
    purchases = purchases.copy()

    def shopping_list_inner(cookies, cps, time_left, building_info) -> Union[str, None]:
        if len(purchases) > 0:
            purchase = purchases.pop(0)
            if purchase == 'None':
                return None
            else:
                return purchase
        else:
            return None

    return shopping_list_inner


""" Register lists """
for item in pathlib.Path("shopping_lists").iterdir():
    strategy = get_shopping_list_strategy_from_file(str(item))
    strategy.__name__ = item.name
    register_strategy(skip=False)(strategy)
