import sys
import math

from cookie_clicker.utils.decorators import *
from cookie_clicker.clicker_state import ClickerState
import cookie_clicker.building_info as building_info
import cookie_clicker.utils as utils


FOREVER = math.sqrt(sys.float_info.max)


@register_competition(skip=False, bigger_is_better=False, duration=10e28)
def time_to_revenue(clicker_state: ClickerState):
    for timestep, _, _, revenue in clicker_state.history:
        if revenue > 1e42:
            return timestep
    if clicker_state.cps > 0:
        return ((1e42 - clicker_state.total_cookies) / clicker_state.cps) + clicker_state.current_time
    else:
        return FOREVER


@register_competition(skip=False)
def profit_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.current_cookies


@register_competition(skip=False)
def revenue_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.total_cookies


@register_competition(skip=False)
def cps_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.cps


@register_competition(skip=False, bigger_is_better=False, duration=10e20)
def time_to_mathematician(clicker_state: ClickerState) -> float:
    my_building_info = building_info.BuildingInfo(utils.Config.DEFAULT_BUILDING_INFO)
    pairs = sorted([(building, my_building_info.get_cost(building=building)) for building in my_building_info.buildings], key=lambda x: x[1], reverse=True)
    required_counts = {building: min(128, int(math.pow(2.0, i))) for i, (building, _) in enumerate(pairs)}

    for timestep, item_name, _, _ in clicker_state.history:
        if item_name in required_counts.keys():
            required_counts[item_name] -= 1
            if all([required <= 0 for _, required in required_counts.items()]):
                return timestep

    return FOREVER
