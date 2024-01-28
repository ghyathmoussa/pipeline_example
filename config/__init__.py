import psycopg2

# Connect to the default PostgreSQL database
default_db = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="ghrefd11!"
)

default_db.autocommit = True