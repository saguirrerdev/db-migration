WITH hired_employees_q AS (
    SELECT
        d.department
        , j.job
        , CASE
            WHEN EXTRACT(QUARTER FROM TO_DATE("datetime" , 'YYYY-MM-DD')) = 1 THEN 'Q1'
            WHEN EXTRACT(QUARTER FROM TO_DATE("datetime" , 'YYYY-MM-DD')) = 2 THEN 'Q2'
            WHEN EXTRACT(QUARTER FROM TO_DATE("datetime" , 'YYYY-MM-DD')) = 3 THEN 'Q3'
            WHEN EXTRACT(QUARTER FROM TO_DATE("datetime" , 'YYYY-MM-DD')) = 4 THEN 'Q4'
        END AS Q
        , count(*)
    FROM hired_employees he
    JOIN departments d ON d.id = he.department_id
    JOIN jobs j ON j.id = he.job_id
    WHERE 1 = 1
    AND EXTRACT(YEAR FROM TO_DATE("datetime" , 'YYYY-MM-DD')) = 2021
    AND he.department_id IS NOT NULL
    AND he.job_id IS NOT NULL
    GROUP BY d.department, j.job, Q
)
SELECT
    department
    , job
    , SUM(CASE WHEN Q = 'Q1' THEN "count" ELSE 0 END) AS Q1
    , SUM(CASE WHEN Q = 'Q2' THEN "count" ELSE 0 END) AS Q2
    , SUM(CASE WHEN Q = 'Q3' THEN "count" ELSE 0 END) AS Q3
    , SUM(CASE WHEN Q = 'Q4' THEN "count" ELSE 0 END) AS Q4
FROM hired_employees_q
GROUP BY department, job
ORDER BY department, job;