""""""
import abc
from typing import Optional
from decimal import Decimal
from cookie_clicker.utils import Registry
from cookie_clicker.buildings.factory import BuildingFactory
from cookie_clicker.clicker_state import ClickerState


class BaseStrategy(abc.ABC):
    """"""

    def __init__(self, name: str = None, skip: bool = False) -> None:
        super(BaseStrategy, self).__init__()
        self.name: str = name or self.__class__.__name__
        self.skip = skip

        Registry.register_strategy(self)

    @abc.abstractmethod
    def __call__(self, state: ClickerState, duration: Decimal) -> Optional[str]:
        """"""
        raise NotImplementedError

    def reset(self) -> None:
        """Don't do anything in the default case"""


class CursorStrategy(BaseStrategy):
    """Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """

    def __init__(self) -> None:
        super(CursorStrategy, self).__init__(name="Cursor", skip=True)

    def __call__(self, state: ClickerState, duration: Decimal) -> str:
        return "Cursor"


class NoneStrategy(BaseStrategy):
    """Always returns None!

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """

    def __init__(self) -> None:
        super(NoneStrategy, self).__init__(name="None", skip=True)

    def __call__(self, state: ClickerState, duration: Decimal) -> None:
        return None
