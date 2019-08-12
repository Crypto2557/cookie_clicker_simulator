"""Here you find some basic strategies for debugging purposes"""

from cookie_clicker.utils.decorators import register_strategy

@register_strategy(skip=True)
def cursor(cookies, cps, time_left, build_info):
    """Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"


@register_strategy(skip=True)
def none(cookies, cps, time_left, building_info):
    """Always returns None!

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None
