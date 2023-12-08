from typing import Dict, List, Union

from clock import Clock


class Schedule:
    def __init__(self, config: List[Dict[str, Union[str, int]]], clock: Clock) -> None:
        self._config = config
        self._clock = clock
        self._slots = self._process_config(config)

    @property
    def setpoint(self):
        current_time = self._clock.time
        if current_time < self._slots[0][0] or current_time >= self._slots[-1][0]:
            return self._slots[-1][1]
        for (start, end) in zip(self._slots, self._slots[1:]):
            if current_time >= start[0] and current_time < end[0]:
                return start[1]

    def _process_config(self, config):
        slots = []
        for slot in config:
            (hours, minutes) = slot["time"].split(":")
            seconds = ((int(hours) * 60) + int(minutes)) * 60
            slots.append([seconds, slot["temperature"]])
        return slots
