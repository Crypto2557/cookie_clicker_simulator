"""Here you find strategies, that are more comprehensive"""
from cookie_clicker.utils.decorators import register_strategy

@register_strategy(skip=False)
def cheap(cookies, cps, time_left, building_info):
    """This strategy buys always the cheapest item."""
    item_list = building_info.buildings

    costs = [(building_info.get_cost(building), building)
             for building in building_info.buildings]
    costs.sort(key=lambda tup: tup[0])

    if costs[0][0] <= (time_left * cps + cookies):
        return costs[0][1]
    else:
        return None


@register_strategy(skip=False)
def expensive(cookies, cps, time_left, building_info):
    """This strategy buys always the most expensive item."""
    item_list = building_info.buildings

    costs = [(building_info.get_cost(building), building)
             for building in building_info.buildings]
    costs.sort(key=lambda tup: tup[0], reverse=True)

    for cost, building in costs:
        if cost <= (time_left * cps + cookies):
            return building
    return None


@register_strategy(skip=False)
def monster(cookies, cps, time_left, building_info):

    def payback_period(cost: float, cookies_in_bank: float, cps: float,
                       cps_building: float) -> float:
        return max(cost - cookies / cps, 0) / cps + cost / cps_building

    if cps == 0.0:
        return 'Cursor'

    item_strings = building_info.buildings
    payback_period_per_item = []
    for item in item_strings:
        payback_period_per_item.append(
            (item,
             payback_period(cost=building_info.get_cost(item),
                            cookies_in_bank=cookies,
                            cps=cps,
                            cps_building=building_info.get_cps(item))))
    payback_period_per_item.sort(key=lambda tup: tup[1])

    best_option = payback_period_per_item[0][0]
    return best_option
