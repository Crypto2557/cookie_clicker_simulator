from .base import CursorStrategy, NoneStrategy
from .impl import CheapStrategy, ExpensiveStrategy, MonsterStrategy
from .from_vec import StrategyFromVec
from .shopping_list import ShoppingListStrategy

CursorStrategy()
NoneStrategy()
CheapStrategy()
ExpensiveStrategy()
MonsterStrategy()

StrategyFromVec(name="irgendwas", dic={
    "Cursor"                : 145-1,
    "Grandma"               : 128,
    "Farm"                  : 128,
    "Mine"                  : 128,
    "Factory"               : 128,
    "Bank"                  : 128,
    "Temple"                : 128,
    "Wizard Tower"          : 128,
    "Shipment"              : 128,
    "Alchemy Lab"           : 64,
    "Portal"                : 44,
    "Time Machine"          : 31,
    "Antimatter Condenser"  : 18,
    "Prism"                 : 12,
    "Chancemaker"           : 8,
    "Fractal Engine"        : 3
})

ShoppingListStrategy.create_from_folder()
