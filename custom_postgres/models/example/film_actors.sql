/* custom_postgres/models/example/film_actors.sql */

SELECT * FROM {{ source('destination_db', 'film_actors') }}