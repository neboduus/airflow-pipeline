## Readme

This repo contains an example of Extract, Transform, and Load (ETL)
pipeline built upon Airflow and Python and deployed on top of Docker.

### Requirements

> Tip: The default amount of memory available for Docker on macOS is often not enough to get Airflow up and running. If 
> enough memory is not allocated, it might lead to the webserver continuously restarting. You should allocate at least 
> 4GB memory for the Docker Engine (ideally 8GB).

You can check if you have enough memory by running this command:

```shell
docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
```

- WIP

### How to use?

- Check your OS user ID and add it to group with ID=`0`

- Run database migrations and create the first user account

```shell
docker compose up airflow-init
```
doc
> The account created has the login `airflow` and the password `airflow`

- Run Airflow

```shell
docker compose up
```

### My notes

- Run CLI command in airflow (must be run in one of the defined airflow-* services)

```shell
docker compose run airflow-worker airflow info
```

