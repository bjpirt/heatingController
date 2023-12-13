from typing import Union


class TemperatureSensor:
    def __init__(self, config: object) -> None:  # pylint: disable=unused-argument
        self.value: Union[float, None] = None

    def read(self) -> Union[float, None]:
        pass
