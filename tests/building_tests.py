from unittest import TestCase

from cookie_clicker.buildings import BuildingFactory, Building


class BaseBuildingTest(TestCase):

    def setUp(self):
        self.factory = BuildingFactory(dict(
            Cursor=dict(cost=15, cps=0.1),
            Grandma=dict(cost=100, cps=0.1),
        ),
                                       growth_factor=1.15)
