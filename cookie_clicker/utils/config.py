import yaml
import abc

from typing import Any, List

try:
    from yaml import CLoader, CDumper
    loader = lambda f: yaml.load(f, Loader=CLoader)
    dumper = lambda data: yaml.dump(data, Dumper=CDumper)

except ImportError:
    from yaml import Loader, Dumper
    loader = lambda f: yaml.load(f, Loader=Loader)
    dumper = lambda data: yaml.dump(data, Dumper=Dumper)


class Config(abc.ABC):

    class Defaults(abc.ABC):
        BUILDING_INFO: str = "configs/buildings.yml"
        SHOPPING_LISTS_FOLDER: str = "shopping_lists"

    MAX_PRECISION: int = 54

    @staticmethod
    def load(fpath: str) -> Any:
        with open(fpath, "r") as f:
            return loader(f)

    @staticmethod
    def dump(fpath: str, content: Any) -> int:
        with open(fpath, "w") as f:
            return f.write(dumper(content))
