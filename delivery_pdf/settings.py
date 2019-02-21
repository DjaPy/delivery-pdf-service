import pathlib
import toml


BASE_DIR = pathlib.Path(__file__).parent.parent
config = BASE_DIR / 'config' / 'delivery_config.toml'


def get_config(path):
    with open(path) as f:
        conf = toml.load(f)
        return conf


config_t = get_config(config)
