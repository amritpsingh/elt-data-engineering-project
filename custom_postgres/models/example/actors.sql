/* custom_postgres/models/example/actors.sql */

SELECT * FROM {{ source('destination_db', 'actors') }}