# Module 1 Homework: Docker & SQL

## Question 1. Understanding Docker images

Run docker with the `python:3.13` image. Use an entrypoint `bash` to interact with the container.

What's the version of `pip` in the image?

- 25.3
- 24.3.1
- 24.2.1
- 23.3.1

## Answer: 25.3

```bash
    docker run -it --rm --entrypoint=bash python:3.13
    python3 -V
    pip3 -V
```


## Question 2. Understanding Docker networking and docker-compose

Given the following `docker-compose.yaml`, what is the `hostname` and `port` that pgadmin should use to connect to the postgres database?

```yaml
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

- postgres:5433
- localhost:5432
- db:5433
- postgres:5432
- db:5432

If multiple answers are correct, select any 

## Answer: db:5432, postgres:5432


## Question 3. Counting short trips

For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a `trip_distance` of less than or equal to 1 mile?

- 7,853
- 8,007
- 8,254
- 8,421

## Answer: 8007

```sql

SET search_path TO public;

SELECT
    COUNT(*)
FROM nov_trips
WHERE lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01'
    AND trip_distance <= 1;

```

## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Only consider trips with `trip_distance` less than 100 miles (to exclude data errors).

Use the pick up time for your calculations.

- 2025-11-14
- 2025-11-20
- 2025-11-23
- 2025-11-25
- 
## Answer -> 2025-11-14

```sql

SET search_path TO public;

SELECT
    lpep_pickup_datetime::DATE AS longest_pickup_distance, trip_distance
FROM nov_trips
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;

```

## Question 5. Biggest pickup zone

Which was the pickup zone with the largest `total_amount` (sum of all trips) on November 18th, 2025?

- East Harlem North
- East Harlem South
- Morningside Heights
- Forest Hills

## Answer -> East Harlem North

```sql

SET search_path TO public;

SELECT
    z."Zone",
    SUM(t.total_amount) AS sum_amount
FROM nov_trips t
LEFT JOIN nov_zones z
ON t."PULocationID" = z."LocationID"
WHERE t.lpep_pickup_datetime::DATE = '2025-11-18'
GROUP BY z."Zone"
ORDER BY sum_amount DESC
LIMIT 5;

```


## Question 6. Largest tip

For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

Note: it's `tip` , not `trip`. We need the name of the zone, not the ID.

- JFK Airport
- Yorkville West
- East Harlem North
- LaGuardia Airport
- 
## Answer -> Yorkville West

``` sql

-- Question 6 -> Answer: Yorkville West
SET search_path TO public;

SELECT
    pz."Zone",
    dz."Zone",
    MAX(tip_amount) AS total_amount
FROM nov_trips t
LEFT JOIN nov_zones pz
ON t."PULocationID" = pz."LocationID"
LEFT JOIN nov_zones dz
ON t."DOLocationID" = dz."LocationID"
WHERE pz."Zone" = 'East Harlem North'
GROUP BY pz."Zone", dz."Zone"
ORDER BY total_amount DESC
LIMIT 1;

```
