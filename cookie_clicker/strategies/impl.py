"""Here you find strategies, that are more comprehensive"""
from cookie_clicker.utils.decorators import register_strategy

@register_strategy(skip=False)
def cheap(cookies, cps, time_left, factory):
    """This strategy buys always the cheapest item."""

    costs = [(factory[building].cost, building)
             for building in factory]
    costs.sort(key=lambda tup: tup[0])

    if costs[0][0] <= (time_left * cps + cookies):
        return costs[0][1]
    else:
        return None


@register_strategy(skip=False)
def expensive(cookies, cps, time_left, factory):
    """This strategy buys always the most expensive item."""
    costs = [(factory[building].cost, building)
             for building in factory]
    costs.sort(key=lambda tup: tup[0], reverse=True)

    for cost, building in costs:
        if cost <= (time_left * cps + cookies):
            return building
    return None


@register_strategy(skip=False)
def monster(cookies, cps, time_left, factory):

    def payback_period(cost: float, cookies_in_bank: float, cps: float,
                       cps_building: float) -> float:
        return max(cost - cookies / cps, 0) / cps + cost / cps_building

    if cps == 0.0:
        return 'Cursor'

    payback_period_per_item = []

    for building_name in factory:
        building = factory[building_name]
        payback_period_per_item.append(
            (building_name,
             payback_period(cost=building.cost,
                            cookies_in_bank=cookies,
                            cps=cps,
                            cps_building=building)))

    payback_period_per_item.sort(key=lambda tup: tup[1])

    best_option = payback_period_per_item[0][0]
    return best_option
