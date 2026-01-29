-- Module 1

-- Question 3 -> Ans: 8007
SET search_path TO public;

SELECT
    COUNT(*)
FROM nov_trips
WHERE lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01'
    AND trip_distance <= 1;

-- Question 3 -> Ans: 2025-11-14
SET search_path TO public;

SELECT
    lpep_pickup_datetime::DATE AS longest_pickup_distance, trip_distance
FROM nov_trips
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;


