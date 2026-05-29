-- 12. Event with Maximum Sessions 
SELECT e.title,
       COUNT(*) AS total_sessions
FROM Events e
JOIN Sessions s ON e.event_id = s.event_id
GROUP BY e.event_id, e.title
HAVING COUNT(*) = (
   SELECT MAX(session_count)
   FROM (
      SELECT COUNT(*) AS session_count
      FROM Sessions
      GROUP BY event_id
   ) x
);