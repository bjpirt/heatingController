
import unittest
from clock import Clock

from schedule import Schedule

config = [
    {"time": "08:00", "temperature": 16},
    {"time": "10:30", "temperature": 12},
    {"time": "21:00", "temperature": 18},
    {"time": "22:15", "temperature": 13},
]


class FakeClock(Clock):
    def __init__(self):
        self.fake_time = 0

    @property
    def time(self) -> int:
        return self.fake_time


class ScheduleTestCase(unittest.TestCase):
    def setUp(self):
        self.fake_clock = FakeClock()
        self.schedule = Schedule(config, self.fake_clock)
        return super().setUp()

    def test_process_config(self):
        self.assertEqual(self.schedule._slots, [
            [28800, 16],
            [37800, 12],
            [75600, 18],
            [80100, 13]
        ])
        self.assertFalse(False)

    def test_setpoint(self):
        self.fake_clock.fake_time = 0
        self.assertEqual(self.schedule.setpoint, 13)

        self.fake_clock.fake_time = 28800
        self.assertEqual(self.schedule.setpoint, 16)

        self.fake_clock.fake_time = 29800
        self.assertEqual(self.schedule.setpoint, 16)

        self.fake_clock.fake_time = 80200
        self.assertEqual(self.schedule.setpoint, 13)
