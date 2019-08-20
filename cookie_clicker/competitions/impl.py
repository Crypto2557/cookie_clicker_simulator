import sys
import math

from decimal import Decimal
D = Decimal

from cookie_clicker.utils.decorators import register_competition
from cookie_clicker.buildings import BuildingFactory
from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.utils import Config


FOREVER = D(math.sqrt(sys.float_info.max))


@register_competition(skip=False, bigger_is_better=False, duration=D(10e28))
def time_to_revenue(clicker_state: ClickerState, target: Decimal = D(1e42)) -> Decimal:
    target = D(target)
    for timestep, _, _, revenue in clicker_state.history:
        if revenue > target:
            return timestep
    if clicker_state.cps > 0:
        return ((target - clicker_state.total_cookies) / clicker_state.cps) + clicker_state.current_time
    else:
        return FOREVER


@register_competition(skip=False)
def profit_at_timestep(clicker_state: ClickerState) -> Decimal:
    return clicker_state.current_cookies


@register_competition(skip=False)
def revenue_at_timestep(clicker_state: ClickerState) -> Decimal:
    return clicker_state.total_cookies


@register_competition(skip=False)
def cps_at_timestep(clicker_state: ClickerState) -> Decimal:
    return clicker_state.cps


@register_competition(skip=False, bigger_is_better=False, duration=D(10e20))
def time_to_mathematician(clicker_state: ClickerState) -> Decimal:
    factory = BuildingFactory(Config.DEFAULT_BUILDING_INFO)
    pairs = sorted([(building_name, factory[building_name].cost) for building_name in factory], key=lambda x: x[1], reverse=True)
    required_counts = {building: min(128, int(math.pow(2.0, i))) for i, (building, _) in enumerate(pairs)}

    for timestep, item_name, _, _ in clicker_state.history:
        if item_name in required_counts.keys():
            required_counts[item_name] -= 1
            if all([required <= 0 for _, required in required_counts.items()]):
                return timestep

    return FOREVER
