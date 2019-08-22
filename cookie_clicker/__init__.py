"""
Registers competitions and strategies and sets precision for Decimals
"""
from decimal import getcontext
from cookie_clicker.utils import Config

from cookie_clicker import competitions
from cookie_clicker import strategies

getcontext().prec = Config.MAX_PRECISION
