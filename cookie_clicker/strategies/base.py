import abc
from cookie_clicker.utils import Registry

class BaseStrategy(abc.ABC):

    def __init__(self, name: str = None, skip: bool = False):
        super(BaseStrategy, self).__init__()
        self.name: str = name or self.__class__.__name__
        self.skip = skip

        Registry.register_strategy(self)

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def reset(self):
        """Don't do anything in the default case"""
        pass


class CursorStrategy(BaseStrategy):
    """Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    def __init__(self):
        super(CursorStrategy, self).__init__(name="Cursor", skip=True)

    def __call__(self, cookies, cps, time_left, factory):
        return "Cursor"


class NoneStrategy(BaseStrategy):
    """Always returns None!

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """

    def __init__(self):
        super(NoneStrategy, self).__init__(name="None", skip=True)

    def __call__(self, cookies, cps, time_left, factory):
        return None
