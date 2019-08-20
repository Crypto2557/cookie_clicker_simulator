import math
from typing import List, Tuple

# from cookie_clicker.buildings import Building

class ClickerState:
    """Simple class to keep track of the game state."""

    def __init__(self) -> None:
        self._total_cookies = 0.0
        self._current_cookies = 15.0
        self._current_time = 0.0
        self._cps = 0.0
        # A list of tuples where each entry in the tuple is:
        # - A time
        # - An item that was bought at that time (or None),
        # - The cost of the item
        # - The total number of cookies produced by that time

        self._history = [(0.0, "", 0.0, 0.0)]

    def __str__(self) -> str:
        """Returns human readable state."""
        return "\n".join([
            f"Time elapsed: {self._current_time:0.1e}",
            f"Cookies baked (all time): {self._total_cookies:0.3e}",
            f"Cookies in bank: {self._current_cookies:0.3e}",
            f"Cookies per second: {self._cps:0.3e}"]) + "\n"

    @property
    def current_cookies(self) -> float:
        return self._current_cookies

    @property
    def cps(self) -> float:
        return self._cps

    @property
    def current_time(self) -> float:
        return self._current_time

    @property
    def total_cookies(self) -> float:
        return self._total_cookies

    @property
    def history(self) -> List[Tuple[float, str, float, float]]:
        return self._history

    def time_until(self, building) -> float:
        """Returns time until you have the given number of cookies.

        Could be 0 if you already have enough cookies.
        Should return a float with no fractional part.
        """

        cookie_diff = building.cost - self._current_cookies
        if cookie_diff > 0:
            return math.ceil(cookie_diff / self._cps)
        else:
            return 0.0

    def wait(self, building) -> None:
        """Waits for the given amount of time and updates state."""
        time = self.time_until(building)
        if time <= 0:
            return

        self._current_time += time
        self._current_cookies += (time * self._cps)
        self._total_cookies += (time * self._cps)

    def buy(self, building) -> None:
        """Waits until the building is buildable,
        Buys a building by updating the state."""

        self.wait(building)

        assert self._current_cookies >= building.cost, \
            f"Cannot buy this building: {building}, because the cost " + \
            f"({building.cost}) are greater than current cookies ({self._current_cookies})"

        self._cps += building.cps
        self._current_cookies -= building.cost

        self._history.append((
            self._current_time,
            building.name,
            building.cost,
            self._total_cookies
        ))

