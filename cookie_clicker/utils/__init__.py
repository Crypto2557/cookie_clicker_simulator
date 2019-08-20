import yaml
import abc

from typing import Any

try:
    from yaml import CLoader, CDumper
    loader = lambda f: yaml.load(f, Loader=CLoader)
    dumper = lambda data: yaml.dump(data, Dumper=CDumper)

except ImportError:
    from yaml import Loader, Dumper
    loader = lambda f: yaml.load(f, Loader=Loader)
    dumper = lambda data: yaml.dump(data, Dumper=Dumper)



class Config(abc.ABC):

    # TODO: move these to Defaults under-class
    DEFAULT_BUILDING_INFO: str = "configs/buildings.yml"
    DEFAULT_SHOPPING_LISTS_FOLDER: str = "shopping_lists"

    @staticmethod
    def load(fpath: str) -> Any:
        with open(fpath, "r") as f:
            return loader(f)

    @staticmethod
    def dump(fpath: str, content: Any) -> int:
        with open(fpath, "w") as f:
            return f.write(dumper(content))

