import asyncio


class TemperatureSensor:
    def __init__(self, pin: int) -> None:
        self.value: int | None = None

    async def read(self) -> float | None:
        pass
