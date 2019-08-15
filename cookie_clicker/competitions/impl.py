import sys
import math

from cookie_clicker.utils.decorators import *
from cookie_clicker.clicker_state import ClickerState


@register_competition(skip=False, bigger_is_better=False, duration=10e28)
def time_to_revenue(clicker_state: ClickerState):
    for timestep, _, _, revenue in clicker_state.history:
        if revenue > 1e42:
            return timestep
    return math.sqrt(sys.float_info.max)


@register_competition(skip=False)
def profit_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.current_cookies


@register_competition(skip=False)
def revenue_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.total_cookies


@register_competition(skip=False)
def cps_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.cps
