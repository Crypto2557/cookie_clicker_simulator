""""""
import unittest

from cookie_clicker.buildings import BuildingFactory


class BaseBuildingTest(unittest.TestCase):
    """"""

    def setUp(self):
        """"""
        self.factory = BuildingFactory(dict(
            Cursor=dict(cost=15, cps=0.1),
            Grandma=dict(cost=100, cps=0.1),
        ),
                                       growth_factor=1.15)


if __name__ == '__main__':
    unittest.main()
