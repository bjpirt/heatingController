from typing import Type
from config import Config
from clock import Clock
from temperature_sensor import TemperatureSensor
from zone_control import ZoneControl
from machine import Pin  # type: ignore


class Thermostat:
    def __init__(self, config: Config, clock: Clock, sensor_class: Type[TemperatureSensor]) -> None:
        self._occupied_timer: int = 0
        self.zones = []
        for (zone, conf) in config.zones.items():
            sensor = sensor_class(conf["sensor"])
            control_pin = Pin(conf["controlPin"])
            self.zones.append(ZoneControl(zone, conf, clock, sensor, control_pin))

    def occupied(self, state: bool):
        for zone in self.zones:
            zone.occupied = state

    def print_debug(self):
        for zone in self.zones:
            zone.print_debug()

    def process(self):
        for zone in self.zones:
            zone.process()
