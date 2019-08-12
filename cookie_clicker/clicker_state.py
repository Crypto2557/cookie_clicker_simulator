import math
from typing import List, Tuple


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
        return (
            f"Time elapsed: {self._current_time:0.1e}\n" +
            f"Cookies baked (all time): {self._total_cookies:0.3e}\n" +
            f"Cookies in bank: {self._current_cookies:0.3e}\n" +
            f"Cookies per second: {self._cps:0.3e}\n")

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

    def time_until(self, cookies: float) -> float:
        """Returns time until you have the given number of cookies.

        Could be 0 if you already have enough cookies.
        Should return a float with no fractional part.
        """
        if cookies - self._current_cookies > 0:
            return math.ceil((cookies - self._current_cookies) / self._cps)
        else:
            return 0.0

    def wait(self, time: float) -> None:
        """Waits for the given amount of time and updates state."""
        if time > 0:
            self._current_time += time
            self._current_cookies += (time * self._cps)
            self._total_cookies += (time * self._cps)

    def buy_item(self, item_name: str, cost: float,
                 additional_cps: float) -> None:
        """Buys an item and update state."""
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._cps += additional_cps
            self._history.append((self._current_time, item_name, cost,
                                  self._total_cookies))
