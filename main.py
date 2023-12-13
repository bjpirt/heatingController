import asyncio
from config import Config
from clock import Clock
from temperature_sensor import DS18B20
from thermostat import Thermostat


async def update_thermostat(thermostat: Thermostat):
    while True:
        thermostat.process()
        await asyncio.sleep_ms(500)


async def print_debug(thermostat: Thermostat):
    while True:
        thermostat.print_debug()
        await asyncio.sleep_ms(2000)


async def loop(t):
    asyncio.create_task(update_thermostat(t))
    asyncio.create_task(print_debug(t))
    while True:
        await asyncio.sleep_ms(1)


def main():
    clock = Clock()
    config = Config()
    t = Thermostat(config, clock, DS18B20)
    asyncio.run(loop(t))
