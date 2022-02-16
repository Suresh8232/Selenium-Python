
from Configurations import config


def get_property(value) -> object:
    return config.common_data[value]
