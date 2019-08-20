from unittest import TestCase

import math
from tempfile import NamedTemporaryFile

from cookie_clicker.buildings import BuildingFactory, Building
from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.utils import Config


class BaseFactoryTest(TestCase):
    def setUp(self):
        super(BaseFactoryTest, self).__init__()

        self.building_info = dict(
            Cursor=dict(cost=15,   cps=0.1),
            Grandma=dict(cost=100, cps=1),
        )

        self.growth_factor = 1.15

class CreationTest(BaseFactoryTest):

    def test_creation_from_dict(self):
        factory = BuildingFactory(self.building_info)

        self.assertIsNotNone(factory)
        self.assertTrue(hasattr(factory, "buildings"))

        self.assertSetEqual(set(factory.buildings), set(self.building_info.keys()),
            "Buildings should be the same as in the dictionary!")

    def test_creation_from_file(self):

        _f = NamedTemporaryFile()
        Config.dump(_f.name, self.building_info)

        factory = BuildingFactory(_f.name)
        factory0 = BuildingFactory(self.building_info)

        self.assertSetEqual(set(factory.buildings), set(self.building_info.keys()),
            "Buildings should be the same as in the file!")

        self.assertSetEqual(set(factory.buildings), set(factory0.buildings),
            "Buildings should be the same as created from dictionary!")

class BuildingTest(BaseFactoryTest):

    def setUp(self):
        super(BuildingTest, self).setUp()
        self.factory = BuildingFactory(
            self.building_info,
            growth_factor=self.growth_factor)


    def test_first_build(self):

        building = self.factory.build("Cursor")

        self.assertIsNotNone(building, "BuildingFactory.build should return something")
        self.assertIsInstance(building, Building)

        self.assertEqual(building.name, "Cursor")
        self.assertEqual(building.cost, self.building_info["Cursor"]["cost"])
        self.assertEqual(building.cps, self.building_info["Cursor"]["cps"])
        self.assertEqual(building.count, 1)

    def test_build_multiple(self):
        building0 = self.factory.build("Cursor")
        building1 = self.factory.build("Cursor")

        self.assertIs(building0, building1, "Should be the same building instance!")

        cost_should = self.building_info["Cursor"]["cost"] * self.growth_factor
        self.assertEqual(building1.cost, math.ceil(cost_should),
            "Building must be more expensive after another build!!")

        self.assertEqual(building1.cps, self.building_info["Cursor"]["cps"],
            "CPS must be the same after another build!")

        self.assertEqual(building1.count, 2)


    def test_build_not_present(self):

        building = self.factory.build("NotCursor")
        self.assertIsNone(building, "BuildingFactory.build should return something")


class StateTest(BaseFactoryTest):

    def setUp(self):
        super(StateTest, self).setUp()
        self.factory = BuildingFactory(
            self.building_info,
            growth_factor=self.growth_factor)

    def test_state_init(self):
        self.assertTrue(hasattr(self.factory, "state"),
            "Factory should have a state!")

        self.assertIsInstance(self.factory.state, ClickerState)

    def test_cps_after_cursor_build(self):
        self.assertEqual(self.factory.state.cps, 0,
            "Initial CPS should be 0!")

        self.factory.build("Cursor")

        cps_should = self.building_info["Cursor"]["cps"]
        self.assertEqual(self.factory.state.cps, cps_should,
            f"CPS with one Cursor should be {cps_should}!")

    def test_cookies_after_cursor_build(self):
        self.assertEqual(self.factory.state.current_cookies, 15,
            "Initial cookies should be 15!")

        self.factory.build("Cursor")

        self.assertEqual(self.factory.state.current_cookies, 0,
            f"Cookies after one Cursor should be 0!")


    def test_time_for_first_cursor(self):

        t = self.factory.time_until("Cursor")
        self.assertEqual(t, 0, "Time for the first cursor should be 0!")

    def test_time_for_next_cursor(self):
        self.factory.build("Cursor")

        t = self.factory.time_until("Cursor")
        cost = self.building_info["Cursor"]["cost"]
        cps = self.building_info["Cursor"]["cps"]

        t_should = cost / cps
        self.assertEqual(t, 0,
            f"Time for the second cursor should be {t_should}!")


