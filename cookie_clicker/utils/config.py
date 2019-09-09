""""""
import abc
import yaml

from typing import Any, List
from decimal import Decimal
D = Decimal

try:
    from yaml import CLoader, CDumper
    LOADER = lambda file: yaml.load(file, Loader=CLoader)
    DUMPER = lambda data: yaml.dump(data, Dumper=CDumper)

except ImportError:
    from yaml import Loader, Dumper
    LOADER = lambda file: yaml.load(file, Loader=Loader)
    DUMPER = lambda data: yaml.dump(data, Dumper=Dumper)


class Config(abc.ABC):
    """ Abstract class holding some of the
    configuration logic and default values """

    class Defaults(abc.ABC):
        """ nested class holding default values """

        BUILDING_INFO: str = "configs/buildings.yml"
        SHOPPING_LISTS_FOLDER: str = "shopping_lists"
        GROWTH_FACTOR: Decimal = D(115) / 100

    MAX_PRECISION: int = 54

    @staticmethod
    def load(fpath: str) -> Any:
        """"""
        with open(fpath, "r") as file:
            return LOADER(file)

    @staticmethod
    def dump(fpath: str, content: Any) -> int:
        """"""
        with open(fpath, "w") as file:
            return file.write(DUMPER(content))
