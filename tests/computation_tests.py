from unittest import TestCase
from decimal import Decimal as D

from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.buildings import BuildingFactory

class RoundingTests(TestCase):

    def setUp(self):
        pass

    def test_time_until_expensive_building(self):
        factory = BuildingFactory(dict(
            Test=dict(
                cost=4879362019269609589837922304,
                cps=1600000
            )
        ))

        state = factory.state
        state.current_cookies = 13743895347200
        state.cps = D(298117875605267) / 10

        building = factory["Test"]
        time = factory.time_until("Test")
        state.wait(time)

        self.assertGreaterEqual(
            state.current_cookies, building.cost,
            f"{building.cost - state.current_cookies} missing!"
        )
