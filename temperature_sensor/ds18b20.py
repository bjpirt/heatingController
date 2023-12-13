from typing import Dict
from machine import Pin  # type: ignore
import onewire  # type: ignore
from ds18x20 import DS18X20  # type: ignore
from .temperature_sensor import TemperatureSensor  # type: ignore


class DS18B20(TemperatureSensor):
    def __init__(self, config: Dict[str, int]) -> None:
        ow = onewire.OneWire(Pin(config["pin"], Pin.PULL_UP))
        self._sensor = DS18X20(ow)
        self.value: float | None = None
        self._setup()
        self.read()

    def _setup(self) -> None:
        self._roms = self._sensor.scan()

    def read(self) -> None:
        if len(self._roms) == 0:
            self.setup()

        if len(self._roms) > 0:
            try:
                self.value = self._sensor.read_temp(self._roms[0])
                self._sensor.convert_temp()
            except onewire.OneWireError:
                self.value = None
