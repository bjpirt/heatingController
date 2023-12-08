class Config:
    def __init__(self) -> None:
        self.zones = {
            "upstairs": {
                "schedule": [
                    {"time": "08:00", "temperature": 16},
                    {"time": "10:00", "temperature": 12},
                    {"time": "21:00", "temperature": 18},
                    {"time": "22:00", "temperature": 13},
                ],
                "sensorPin": 12,
                "controlPin": 10,
                "unoccupiedTemperature": 10
            },
            "downstairs": {
                "schedule": [
                    {"time": "08:00", "temperature": 16},
                    {"time": "10:00", "temperature": 12},
                    {"time": "21:00", "temperature": 18},
                    {"time": "22:00", "temperature": 13},
                ],
                "sensorPin": 13,
                "controlPin": 11,
                "unoccupiedTemperature": 10
            }
        }