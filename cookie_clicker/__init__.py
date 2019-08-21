from decimal import getcontext
from cookie_clicker.utils import Config

getcontext().prec = Config.MAX_PRECISION
