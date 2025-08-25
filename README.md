# Datawrap

Docker-wrapped data management with dbt and postgresql. A local version of postgresql must be running.
Sample data and example transactions provided by `jaffle-shop-classic` from dbt-labs.

## Usage

```bash
git clone https://github.com/msyvr/datawrap
cd datawrap
```

- update `.env` file

```bash
docker compose up -d --build
```

- configure `profiles.yml`

```bash
docker exec -it dbt_core /bin/bash
```

```bash
dbt deps

# dbt project setup (sample data)
dbt clean
dbt snapshot
dbt run
dbt test

# dbt docs
dbt docs generate
dbt docs serve --port 8080 --host 0.0.0.0
```

## Database

PostgreSQL: data warehouse for raw and transformed data.

## Database interactions

Data transforms, versioning (schema, snapshots), testing are managed by dbt.

## Deploy

Containerized deploy with Docker for isolated, secure data management.

## Usage: details

Prereqs: Python, Docker, PostgreSQL

```bash
git clone https://github.com/msyvr/datawrap.git
cd datawrap
```

- Create your own `.env` file based on `.env_example` and update fields to work with your local environment.
- Check that Docker is running.

### Start the containers:

```bash
docker compose up -d --build
```

Before dbt commands can run, configure the database connection: `profiles.yml`

### Docker exec into the container to have shell access:

```bash
docker exec -it dbt_core /bin/bash
```

### Execute dbt commands:

```bash
# dbt project set up and build
dbt deps
dbt clean
dbt snapshot
dbt run
dbt test

# dbt docs
dbt docs generate
dbt docs serve --port 8080 --host 0.0.0.0
```

### Snapshots

Create snapshots from the `dbt_core` container (or `make sh`). Example records update:

```bash
python /usr/app/dbt_project/database/scripts/update_data.py
```

Run the snapshot, (re)create models:

```bash
dbt snapshot
dbt run
```

Review updates:

```bash
psql -h dbt_postgres -U dbtuser -d dbtpg
```

If necessary, verify the password in `.env` and update as required:

```bash
Password for user dbtuser:
```

Test query:

```sql
select * from snapshots.customers_snapshot where customer_id = 82;
```

## Convenience scripts

Optional, to circumvent running docker commands explicitly:

- `make build`: build images
- `make docker-up`: start containers
- `make up`: `make build` + `make docker-up`
- `make down`: stop containers, remove containers
- `make volumes`: view Docker volumes
- `make restart`: stop containers, remove volumes, restart project
- `make sh`: start a shell within the `dbt_core` container

## Troubleshooting

Container issues? Try a rebuild:

```bash
docker compose down
docker compose up -d --build
```

... and/or review logs:

```bash
docker logs dbt_core
docker logs pg_init_data_load
```

## Resources

- [slowly changing dimensions](https://www.phdata.io/blog/how-to-slowly-change-dimensions-with-snapshots-in-dbt/): updates propagate to snapshots
