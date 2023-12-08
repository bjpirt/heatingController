from config import Config
from clock import Clock
from thermostat import Thermostat


def main():
    clock = Clock()
    config = Config()
    t = Thermostat(config, clock)

    while True:
        t.process()
