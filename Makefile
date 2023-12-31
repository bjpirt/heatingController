.PHONY: start-mosquitto
start-mosquitto:
	docker run -d --name mosquitto -p 1883:1883 -v ${PWD}/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto

.PHONY: stop-mosquitto
stop-mosquitto:
	docker stop mosquitto

.PHONY: upload
upload:
	ampy put clock.py
	ampy put config.py
	ampy put schedule.py
	ampy put thermostat.py
	ampy put temperature_sensor
	ampy put stubs/typing.py
	ampy put zone_control.py
	ampy put main.py

.PHONY: test
test:
	python -m unittest --verbose

.PHONY: lint
lint:
	pylint --recursive=y temperature_sensor ./*.py

.PHONY: ruff
ruff:
	ruff check .

.PHONY: mypy
mypy:
	mypy --exclude scripts --exclude test --exclude stubs --check-untyped-defs .

.PHONY: check
check: lint ruff mypy
