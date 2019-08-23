""""""
import unittest
import math
from tempfile import NamedTemporaryFile
from decimal import Decimal

from cookie_clicker.buildings import Building
from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.utils import Config

D = Decimal


class BaseFactoryTest(unittest.TestCase):
    """"""

    def setUp(self):
        super(BaseFactoryTest, self).__init__()

        self.building_info = dict(
            Cursor=dict(cost=D(15), cps=D(str(0.1))),
            Grandma=dict(cost=D(100), cps=D(1)),
        )

        self.growth_factor = D(115) / 100

    def new_factory(self, building_info=None, **kwargs):
        self.state = ClickerState.new(building_info or self.building_info,
                                  **kwargs)
        return self.state.factory

class CreationTest(BaseFactoryTest):
    """"""

    def test_creation_from_dict(self):
        factory = self.new_factory()

        self.assertIsNotNone(factory)
        self.assertTrue(hasattr(factory, "buildings"))

        self.assertSetEqual(
            set(factory.buildings), set(self.building_info.keys()),
            "Buildings should be the same as in the dictionary!")

    def test_creation_from_file(self):

        _file = NamedTemporaryFile()
        Config.dump(_file.name, self.building_info)

        factory = self.new_factory(_file.name)
        factory0 = self.new_factory()

        self.assertSetEqual(set(factory.buildings),
                            set(self.building_info.keys()),
                            "Buildings should be the same as in the file!")

        self.assertSetEqual(
            set(factory.buildings), set(factory0.buildings),
            "Buildings should be the same as created from dictionary!")


class BuildingTest(BaseFactoryTest):
    """"""

    def setUp(self):
        super(BuildingTest, self).setUp()
        self.factory = self.new_factory(growth_factor=self.growth_factor)

    def test_first_build(self):

        building = self.factory["Cursor"]

        self.assertIsNotNone(building,
                             "BuildingFactory.build should return something")
        self.assertIsInstance(building, Building)

        self.assertEqual(building.name, "Cursor")
        self.assertEqual(building.cost, self.building_info["Cursor"]["cost"])
        self.assertEqual(building.cps, self.building_info["Cursor"]["cps"])

        self.state.buy("Cursor")
        self.assertEqual(building.count, 1)

    def test_build_multiple(self):
        building0 = self.state.buy("Cursor")
        building1 = self.factory["Cursor"]

        self.assertIs(building0, building1,
                      "Should be the same building instance!")

        cost_should = self.building_info["Cursor"]["cost"] * self.growth_factor
        self.assertEqual(
            building1.cost, math.ceil(cost_should),
            "Building must be more expensive after another build!!")

        self.assertEqual(building1.cps, self.building_info["Cursor"]["cps"],
                         "CPS must be the same after another build!")

        building1 = self.state.buy("Cursor")
        self.assertEqual(building1.count, 2)

    def test_build_not_present(self):

        building = self.state.buy("NotCursor")
        self.assertIsNone(building,
                          "BuildingFactory.build should return something")


class StateTest(BaseFactoryTest):
    """"""

    def setUp(self):
        super(StateTest, self).setUp()
        self.factory = self.new_factory(growth_factor=self.growth_factor)

    @unittest.skip
    def test_state_init(self):
        self.assertTrue(hasattr(self.factory, "state"),
                        "Factory should have a state!")

        self.assertIsInstance(self.factory.state, ClickerState)

    def test_cps_after_cursor_build(self):
        self.assertEqual(self.state.cps, 0, "Initial CPS should be 0!")

        self.state.buy("Cursor")

        cps_should = self.building_info["Cursor"]["cps"]
        self.assertEqual(self.state.cps, cps_should,
                         f"CPS with one Cursor should be {cps_should}!")

    def test_cookies_after_cursor_build(self):
        self.assertEqual(self.state.current_cookies, 15,
                         "Initial cookies should be 15!")

        self.state.buy("Cursor")

        self.assertEqual(self.state.current_cookies, 0,
                         f"Cookies after one Cursor should be 0!")

    def test_time_for_first_cursor(self):

        time = self.state.time_until(self.factory["Cursor"])
        self.assertEqual(time, 0, "Time for the first cursor should be 0!")

    def test_time_for_next_cursor(self):
        building = self.state.buy("Cursor")

        time = self.state.time_until(self.factory["Cursor"])
        cost = building.cost
        cps = self.state.cps

        time_should = cost / cps
        self.assertEqual(
            time, time_should,
            f"Time for the second cursor should be {time_should}!")


if __name__ == '__main__':
    unittest.main()
