""""""
import unittest

from decimal import Decimal

from cookie_clicker.buildings import BuildingFactory

D = Decimal


class BaseBuildingTest(unittest.TestCase):
    """"""

    def setUp(self):
        """"""
        info = dict(
            Cursor=dict(cost=15, cps=0.1),
            Grandma=dict(cost=100, cps=0.1),
        )
        self.factory = BuildingFactory(info, growth_factor=1.15)


if __name__ == '__main__':
    unittest.main()
