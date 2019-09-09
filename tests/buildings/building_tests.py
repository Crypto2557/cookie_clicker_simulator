""""""
import unittest

from decimal import Decimal

from cookie_clicker.buildings import BuildingFactory
from cookie_clicker.utils import Config

D = Decimal


class BaseBuildingTest(unittest.TestCase):
    """"""

    def setUp(self):
        """"""
        info = dict(
            Cursor=dict(cost=15, cps=0.1),
            Grandma=dict(cost=100, cps=0.1),
        )
        self.factory = BuildingFactory(info, growth_factor=Config.Defaults.GROWTH_FACTOR)


if __name__ == '__main__':
    unittest.main()
