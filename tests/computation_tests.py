from unittest import TestCase
from decimal import Decimal as D

from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.buildings import BuildingFactory


class RoundingTests(TestCase):

    def test_time_until_expensive_building(self):
        cases = [
            (D(4879362019269609589837922304), D(13743895347200),
             D(298117875605267) / 10),
            (D(632768350294440421670318569200000000000), D(18100000000000),
             D(61878254334020)),
        ]

        for i, (cost, current_cookies, cps) in enumerate(cases):

            factory = BuildingFactory(dict(Test=dict(cost=cost, cps=1600000)))

            state = factory.state
            state.current_cookies = current_cookies
            state.cps = cps

            building = factory["Test"]
            time = factory.time_until("Test")
            state.wait(time)

            self.assertGreaterEqual(
                state.current_cookies, building.cost,
                f"[case {i}] {building.cost - state.current_cookies} missing!")
