from decimal import getcontext
from cookie_clicker.utils import Config

# registers competitions and strategies
from cookie_clicker import competitions
from cookie_clicker import strategies

getcontext().prec = Config.MAX_PRECISION
