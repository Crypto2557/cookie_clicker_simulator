import math
from dataclasses import dataclass, field
from typing import List, Tuple, Any
from decimal import Decimal

D = Decimal

@dataclass
class ClickerState:
    """Simple class to keep track of the game state."""

    # A list of tuples where each entry in the tuple is:
    # - A time
    # - An item that was bought at that time (or None),
    # - The cost of the item
    # - The total number of cookies produced by that time
    total_cookies: Decimal = D(0)
    current_cookies: Decimal = D(15)
    current_time: Decimal = D(0)
    cps: Decimal = D(0)

    history: List[Tuple[Decimal, str, Decimal, Decimal]] = field(
        init=False, repr=False,
        default_factory=lambda: [(D(0), "", D(0), D(0))])

    def __str__(self) -> str:
        """Returns human readable state."""
        return "\n".join([
            f"Time elapsed: {self.current_time:0.1e}",
            f"Cookies baked (all time): {self.total_cookies:0.3e}",
            f"Cookies in bank: {self.current_cookies:0.3e}",
            f"Cookies per second: {self.cps:0.3e}"]) + "\n"


    def time_until(self, building: Any) -> Decimal:
        """Returns time until you have the given number of cookies.

        Could be 0 if you already have enough cookies.
        Should return a Decimal with no fractional part.
        """

        cookie_diff = building.cost - self.current_cookies
        if cookie_diff > 0:
            return D(math.ceil(cookie_diff / self.cps))
        else:
            return D(0)

    def wait_for_building(self, building: Any) -> None:
        """Waits for the given amount of time and updates state
        based on the building.
        """
        time = self.time_until(building)
        # print(f"Waiting {time} to build {building.name} ({building.count})")
        self.wait(time)

    def wait(self, time: Decimal) -> None:
        """Waits for the given amount of time and updates state."""
        if time <= 0:
            return

        self.current_time += time
        self.current_cookies += (time * self.cps)
        self.total_cookies += (time * self.cps)

    def buy(self, building: Any) -> None:
        """Waits until the building is buildable,
        Buys a building by updating the state."""

        self.wait_for_building(building)

        assert self.current_cookies >= building.cost, \
            f"Cannot buy \"{building.name}\", because the cost " + \
            f"({building.cost}) are greater than current cookies ({self.current_cookies}). " + \
            f"Diff: {self.current_cookies - building.cost}"

        self.cps = self.cps + building.cps
        self.current_cookies -= building.cost

        self.history.append((
            self.current_time,
            building.name,
            building.cost,
            self.total_cookies
        ))

