from decimal import Decimal
D = Decimal

from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.competitions.base import BaseCompetition

class ProfitCompetition(BaseCompetition):
    def __init__(self):
        super(ProfitCompetition, self).__init__(name="profit_at_timestep")

    def __call__(self, clicker_state: ClickerState) -> Decimal:
        return clicker_state.current_cookies

class RevenueCompetition(BaseCompetition):
    def __init__(self):
        super(RevenueCompetition, self).__init__(name="revenue_at_timestep")

    def __call__(self, clicker_state: ClickerState) -> Decimal:
        return clicker_state.total_cookies

class CPSCompetition(BaseCompetition):
    def __init__(self):
        super(CPSCompetition, self).__init__(name="cps_at_timestep")

    def __call__(self, clicker_state: ClickerState) -> Decimal:
        return clicker_state.cps

class TimeToRevenueCompetition(BaseCompetition):
    def __init__(self, target: Decimal = D(1e42)):
        super(TimeToRevenueCompetition, self).__init__(
            name="time_to_revenue",
            bigger_is_better=False,
            duration=D(1e28))

        self.target = D(target)

    def __call__(self, clicker_state: ClickerState) -> Decimal:
        for timestep, _, _, revenue in clicker_state.history:
            if revenue > self.target:
                return timestep

        if clicker_state.cps > 0:
            return ((self.target - clicker_state.total_cookies) / clicker_state.cps) + clicker_state.current_time
        else:
            return self.FOREVER
