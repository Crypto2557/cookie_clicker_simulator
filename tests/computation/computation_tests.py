""""""
import unittest
from decimal import Decimal as D

from cookie_clicker.buildings import BuildingFactory


class RoundingTests(unittest.TestCase):
    """"""

    def test_t_until_expensive_building(self):
        """"""
        cases = [
            (D(4879362019269609589837922304), D(13743895347200),
             D(298117875605267) / 10),
            (D(632768350294440421670318569200000000000), D(18100000000000),
             D(61878254334020)),
        ]

        for i, (cost, current_cookies, cps) in enumerate(cases):

            state = ClickerState(dict(Test=dict(cost=cost, cps=1600000)))

            state.current_cookies = current_cookies
            state.cps = cps

            building = state.factory["Test"]
            time = state.time_until(building)
            state.wait(time)

            self.assertGreaterEqual(
                state.current_cookies, building.cost,
                f"[case {i}] {building.cost - state.current_cookies} missing!")


if __name__ == '__main__':
    unittest.main()
