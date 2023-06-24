.PHONY: unit-test
unit-test:
	env/bin/python3 -m pytest -vv --log-cli-level=DEBUG

.PHONY: build-containers
build-containers:
	cd data_ingestor && docker build -t data_ingestor:0.0.1 .

.PHONY: create_env
create_env:
	python -m venv env

.PHONY: init
init: create_env
	env/bin/pip install -r requirements.txt
