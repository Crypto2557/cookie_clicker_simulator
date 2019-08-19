import yaml
import abc

try:
    from yaml import CLoader
    loader = lambda f: yaml.load(f, Loader=CLoader)
except ImportError:
    from yaml import Loader
    loader = lambda f: yaml.load(f, Loader=Loader)


def read_config_file(fpath: str) -> dict:
    with open(fpath) as f:
        return loader(f)

class Config(abc.ABC):
    DEFAULT_BUILDING_INFO: str = "configs/buildings.yml"
    DEFAULT_SHOPPING_LISTS_FOLDER: str = "shopping_lists"
