-- Module 1

-- Question 3 -> Ans: 8007
SET search_path TO public;

SELECT
    COUNT(*)
FROM nov_trips
WHERE lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01'
    AND trip_distance <= 1;

-- Question 4 -> Ans: 2025-11-14
SET search_path TO public;

SELECT
    lpep_pickup_datetime::DATE AS longest_pickup_distance, trip_distance
FROM nov_trips
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;

-- Question 5 -> Answer: East Harlem North
SET search_path TO public;

SELECT
    lpep_pickup_datetime::DATE AS longest_pickup_distance, trip_distance
FROM nov_trips
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;


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
