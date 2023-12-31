from lib import PersistentConfig
try:
    from initial_config import config   # type: ignore
except ImportError:
    config = {}


class Config(PersistentConfig):
    def __init__(self) -> None:
        self.zones = {
            "upstairs": {
                "schedule": [
                    {"time": "08:00", "temperature": 16},
                    {"time": "10:00", "temperature": 12},
                    {"time": "21:00", "temperature": 18},
                    {"time": "22:00", "temperature": 13},
                ],
                "sensor": {"pin": 18},
                "controlPin": 10,
                "unoccupiedTemperature": 10,
                "boostTemperature": 18,
                "protectTemperature": 10
            },
            "downstairs": {
                "schedule": [
                    {"time": "08:00", "temperature": 16},
                    {"time": "10:00", "temperature": 12},
                    {"time": "21:00", "temperature": 18},
                    {"time": "22:00", "temperature": 13},
                ],
                "sensor": {"pin": 18},
                "controlPin": 11,
                "unoccupiedTemperature": 10,
                "boostTemperature": 18,
                "protectTemperature": 10
            }
        }

        self.wifi_ssid = ""
        self.wifi_password = ""
        self.wifi_enabled = False

        super().__init__(config)
