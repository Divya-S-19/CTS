-- 16. Unregistered Active Users 
SELECT
    u.user_id,
    u.full_name,
    u.email,
    u.registration_date
FROM Users u
LEFT JOIN Registrations r
    ON u.user_id = r.user_id
WHERE r.user_id IS NULL
AND u.registration_date >= CURDATE() - INTERVAL 30 DAY;