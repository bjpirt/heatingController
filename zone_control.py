from typing import Dict, Union
from clock import Clock
from machine import Pin  # type: ignore
from schedule import Schedule
from temperature_sensor.temperature_sensor import TemperatureSensor
import time


class ZoneControl:
    def __init__(self, name: str, config: Dict, clock: Clock, sensor: TemperatureSensor, control_pin: Pin) -> None:
        self.name = name
        self.occupied: bool = True
        self._override: Union[bool, None] = None
        self._override_time_end: int = 0
        self._config = config
        self._control_pin = control_pin
        self._sensor = sensor
        self._schedule = Schedule(config["schedule"], clock)

    @property
    def temperature(self):
        return self._sensor.value

    def override(self, state: bool, interval: int) -> None:
        self._override = state
        self._override_time_end = int(time.time()) + interval

    @property
    def setpoint(self):
        if not self.occupied:
            return self._config["unoccupiedTemperature"]

        if self._override is not None:
            if time.time() < self._override_time_end:
                return self._config["boostTemperature"] if self._override else self._config["unoccupiedTemperature"]
            else:
                self._override = None

        return self._schedule.setpoint

    def print_debug(self):
        print(f"{self.name} {self.temperature} {self.setpoint}")

    def process(self):
        self._sensor.read()
        if self.temperature is not None and self.temperature < self.setpoint:
            self._control_pin.on()
        else:
            self._control_pin.off()
