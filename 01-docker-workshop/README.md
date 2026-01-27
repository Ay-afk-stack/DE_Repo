# Docker Workshop

## The NYC Taxi Dataset

URL = [tqdm](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz)

## Running PostgreSQL in a Container

Create a folder anywhere you'd like for Postgres to store data in. We will use the example folder `ny_taxi_postgres_data`. Here's how to run the container:

```bash
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
```

### Explanation of Parameters

- `-e` sets environment variables (user, password, database name)
- `-v ny_taxi_postgres_data:/var/lib/postgresql` creates a **named volume**
  - Docker manages this volume automatically
  - Data persists even after container is removed
  - Volume is stored in Docker's internal storage
- `-p 5432:5432` maps port 5432 from container to host
- `postgres:18` uses PostgreSQL version 18 (latest as of Dec 2025)

## Connecting to PostgreSQL

Once the container is running, we can log into our database with [pgcli](https://www.pgcli.com/).

Install pgcli:

```bash
uv add --dev pgcli
```

The `--dev` flag marks this as a development dependency (not needed in production). It will be added to the `[dependency-groups]` section of `pyproject.toml` instead of the main `dependencies` section.

Now use it to connect to Postgres:

```bash
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

- `uv run` executes a command in the context of the virtual environment
- `-h` is the host. Since we're running locally we can use `localhost`.
- `-p` is the port.
- `-u` is the username.
- `-d` is the database name.
- The password is not provided; it will be requested after running the command.

When prompted, enter the password: `root`
