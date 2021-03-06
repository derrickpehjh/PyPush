"""Bluetooth Low Energy library abstraction layer.

The API object returned is expected to conform to the PyPush.iApi interface.
"""

from .. import const

from . import (
    iApi,
    exceptions,
    bgapi,
)

def getBgApi(config):
    from . import bgapi
    return bgapi.API(config)

def getPyBluezApi(config):
    from . import bluez
    return bluez.API(config)


def getLib(config):
    """Automatically detect & deploy one of supported Python BLE libs."""
    if config["driver"] == "bgapi":
        rv = getBgApi(config)
    elif config["driver"] == "pybluez":
        rv = getPyBluezApi(config)
    else:
        raise NotImplementedError(config)

    assert isinstance(rv, iApi.iApi)
    return rv
