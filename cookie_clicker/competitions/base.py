import abc
import sys
import math

from decimal import Decimal
D = Decimal

from cookie_clicker.clicker_state import ClickerState
from cookie_clicker.utils import Registry

class BaseCompetition(abc.ABC):
    FOREVER: Decimal = D(math.sqrt(sys.float_info.max))

    def __init__(self,
            name: str = None,
            skip: bool = False,
            bigger_is_better: bool = True,
            duration: Decimal = D(1e10)) -> None:
        super(BaseCompetition, self).__init__()

        self.name = name or self.__class__.__name__
        self.skip = skip
        self.bigger_is_better = bigger_is_better
        self.duration = duration

        Registry.register_competition(self)

    @abc.abstractmethod
    def __call__(self, clicker_state: ClickerState) -> Decimal:
        raise NotImplementedError



