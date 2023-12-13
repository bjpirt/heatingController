import asyncio
from config import Config
from clock import Clock
from temperature_sensor import DS18B20
from thermostat import Thermostat


async def update_thermostat(thermostat: Thermostat):
    while True:
        thermostat.process()
        await asyncio.sleep(0.5)


async def print_debug(thermostat: Thermostat):
    while True:
        thermostat.print_debug()
        await asyncio.sleep(2)


async def loop(t):
    asyncio.create_task(update_thermostat(t))
    asyncio.create_task(print_debug(t))
    while True:
        await asyncio.sleep(0.001)


def main():
    clock = Clock()
    config = Config()
    t = Thermostat(config, clock, DS18B20)
    asyncio.run(loop(t))
