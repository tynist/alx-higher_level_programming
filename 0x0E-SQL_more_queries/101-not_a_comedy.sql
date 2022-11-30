-- List all shows without genre 'Comedy' in 'hbtn_0d_tvshows'
-- 'tv_genres' table contains only one record where name = Comedy
SELECT s.title
FROM tv_shows s
WHERE s.title NOT IN (
      SELECT s.title
      FROM tv_shows s
      INNER JOIN tv_show_genres m ON s.id = m.show_id
      INNER JOIN tv_genres g ON m.genre_id = g.id
      WHERE g.name = 'Comedy'
)
ORDER BY s.title ASC;
