-- SQL lists all shows without the genre Comedy in the database
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
      SELECT tv_shows.title
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id=tv_show_genres.genre_id
      AND tv_show_genres.show_id=tv_shows.id
      AND tv_genres.name='Comedy')
ORDER BY tv_shows.title;
