from typing import Dict
from clock import Clock
from machine import Pin
from schedule import Schedule
from temperature_sensor import TemperatureSensor


class ZoneControl:
    def __init__(self, name: str, config: Dict, clock: Clock) -> None:
        self.name = name
        self.occupied: bool = True
        self.override: bool | None = None
        self.override_time: int = 0
        self._control_pin = Pin(config["controlPin"])
        self._sensor = TemperatureSensor(config["sensorPin"])
        self._schedule = Schedule(config["schedule"], clock)

    @property
    def temperature(self):
        return self._sensor.value

    @property
    def setpoint(self):
        return self._schedule.setpoint

    def process(self):
        pass
