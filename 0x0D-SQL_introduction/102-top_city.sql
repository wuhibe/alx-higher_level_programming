-- Top 3 Cities
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month >= 7 AND month < 9 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
