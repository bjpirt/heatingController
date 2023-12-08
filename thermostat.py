from config import Config
from clock import Clock
from zone_control import ZoneControl


class Thermostat:
    def __init__(self, config: Config, clock: Clock) -> None:
        self._occupied_timer: int = 0
        self.zones = []
        for (zone, conf) in config.zones.items():
            self.zones.append(ZoneControl(zone, conf, clock))

    @property
    def occupied(self, state: bool):
        for zone in self.zones:
            zone.occupied = state

    def process(self):
        for zone in self.zones:
            zone.process()
