WITH hires_by_department AS (
    SELECT
        d.id
        , d.department
        , COUNT(*) AS hired
    FROM hired_employees he
    JOIN departments d ON d.id = he.department_id
    WHERE 1 = 1
    AND EXTRACT(YEAR FROM TO_DATE("datetime" , 'YYYY-MM-DD')) = 2021 
    -- AND he.department_id IS NOT NULL
    -- AND he.job_id IS NOT NULL
    GROUP BY d.id, d.department
)
SELECT
    *
FROM hires_by_department
WHERE hired > (SELECT AVG(hired) FROM hires_by_department)
ORDER BY hired DESC