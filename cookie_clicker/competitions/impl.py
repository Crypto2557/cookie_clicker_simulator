from cookie_clicker.utils.decorators import *
from cookie_clicker.clicker_state import ClickerState


@register_competition(skip=False)
def revenue_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.total_cookies


@register_competition(skip=False)
def profit_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.current_cookies

@register_competition(skip=False)
def cps_at_timestep(clicker_state: ClickerState) -> float:
    return clicker_state.cps
