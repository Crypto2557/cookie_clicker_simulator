""" Shopping List strategy """
import pathlib
from cookie_clicker.utils.decorators import register_strategy


def get_shopping_list_strategy_from_file(shopping_list_path):
    with open(shopping_list_path) as shopping_list:
        purchases = [str(x).strip() for x in shopping_list]

    return get_shopping_list_strategy_from_list(purchases)


def get_shopping_list_strategy_from_list(purchases):
    purchases = purchases.copy()

    def shopping_list_inner(cookies, cps, time_left, building_info):
        if len(purchases) > 0:
            purchase = purchases.pop(0)
            return purchase
        else:
            return None

    return shopping_list_inner


""" Register lists """
for item in pathlib.Path("shopping_lists").iterdir():
    strategy = get_shopping_list_strategy_from_file(item)
    strategy.__name__ = item.name
    register_strategy(skip=False)(strategy)
