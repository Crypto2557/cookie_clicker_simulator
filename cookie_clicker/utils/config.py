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
    """"""

    class Defaults(abc.ABC):
        """"""
        BUILDING_INFO: str = "configs/buildings.yml"
        SHOPPING_LISTS_FOLDER: str = "shopping_lists"
        GROWTH_FACTOR: Decimal = D(1.15)

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
