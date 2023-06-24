.PHONY: unit-test
unit-test:
	docker run unit_test:0.0.1

.PHONY: build-data-ingestor-containers
build-data-ingestor-containers:
	cd data_ingestor && docker build -t data_ingestor:0.0.1 .

.PHONY: build-unittest-container
build-unittest-container:
	docker build -f unittest.Dockerfile -t unit_test:0.0.1 .

.PHONY: build-containers
build-containers: build-unittest-container build-data-ingestor-containers

.PHONY: create_env
create_env:
	python3.8 -m venv env

.PHONY: install-data-ingestor-requirements
install-data-ingestor-requirements:
	env/bin/pip install -r data_ingestor/requirements.txt

.PHONY: install-etl-pipeline-requirements
install-etl-pipeline-requirements:
	env/bin/pip install -r etl/requirements.txt

.PHONY: init
init: create_env install-etl-pipeline-requirements install-data-ingestor-requirements

.PHONY: deploy
deploy:
	docker-compose up

.PHONY: integration-test
integration-test:
	docker exec -it data-engineering-pipeline-airflow-worker-1 airflow dags test etl_pipeline
