from typing import Dict, Union
try:
    from machine import Pin  # type: ignore
    import onewire  # type: ignore
    from ds18x20 import DS18X20  # type: ignore
except ModuleNotFoundError:
    pass
from .temperature_sensor import TemperatureSensor


class DS18B20(TemperatureSensor):
    def __init__(self, config: object) -> None:
        if type(config) == Dict and "pin" in config:
            ow = onewire.OneWire(Pin(config["pin"], Pin.PULL_UP))
            self._sensor = DS18X20(ow)
        else:
            raise ValueError()
        self.value: Union[float, None] = None
        self._setup()
        self.read()
        super().__init__(config)

    def _setup(self) -> None:
        self._roms = self._sensor.scan()

    def read(self) -> None:
        if len(self._roms) == 0:
            self._setup()

        if len(self._roms) > 0:
            try:
                self.value = self._sensor.read_temp(self._roms[0])
                self._sensor.convert_temp()
            except onewire.OneWireError:
                self.value = None
