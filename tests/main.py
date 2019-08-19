#!/usr/bin/env python
if __name__ != '__main__': raise Exception("Do not import me!")

import sys
from os.path import abspath, dirname, join

addons_dir = abspath(join(abspath(dirname(__file__)), ".."))
sys.path.insert(0, addons_dir)

### Import tests like this:
# from tests.[test_module] import *

from tests.dummy import *

import unittest
unittest.main()
