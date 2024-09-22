/* custom_postgres/models/example/films.sql */

SELECT * FROM {{ source('destination_db', 'films') }}