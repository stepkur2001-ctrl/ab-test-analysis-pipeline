SELECT u.user_id, u."group", COALESCE(SUM(r.revenue), 0) AS revenue_total, CASE WHEN count(r.event_id) > 0 THEN 1 ELSE 0 END AS converted
FROM users AS u
LEFT JOIN raw_events_expanded AS r ON u.user_id = r.user_id
GROUP BY u.user_id, u."group";
