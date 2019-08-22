""""""
from unittest import TestCase, skip


class DummyTestCase(TestCase):
    """"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @skip
    def test_skipped(self):
        self.assertFalse(True)  #pylint: disable=redundant-unittest-assert

    def test_failing_test(self):
        self.assertFalse(True)  #pylint: disable=redundant-unittest-assert

    def test_passing_test(self):
        self.assertTrue(True)  #pylint: disable=redundant-unittest-assert
