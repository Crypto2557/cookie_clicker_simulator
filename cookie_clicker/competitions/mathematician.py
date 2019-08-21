import copy

from decimal import Decimal
D = Decimal

from .base import BaseCompetition
from cookie_clicker.buildings import BuildingFactory
from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.utils import Config

class Mathematician(BaseCompetition):
    def __init__(self) -> None:
        super(Mathematician, self).__init__(
            name="time_to_mathematician",
            bigger_is_better=False,
            duration=D(1e20)
        )

        factory = BuildingFactory(Config.Defaults.BUILDING_INFO)
        buildings_with_costs = [(building_name, factory[building_name].cost) for building_name in factory]
        pairs = sorted(buildings_with_costs, key=lambda x: x[1], reverse=True)
        self.counts = {building: min(128, 2**i) for i, (building, _) in enumerate(pairs)}

    def __call__(self, clicker_state: ClickerState) -> Decimal:
        required_counts = copy.deepcopy(self.counts)

        for timestep, item_name, _, _ in clicker_state.history:
            if item_name in required_counts:
                required_counts[item_name] -= 1
                if all([required <= 0 for required in required_counts.values()]):
                    return timestep

        return self.FOREVER
