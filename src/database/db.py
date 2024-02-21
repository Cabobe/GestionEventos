import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host=config('PG_SQL_HOST'),
            port=config('PG_SQL_PORT'),
            database=config('PG_SQL_DATABASE'),
            user=config('PG_SQL_USER'),
            password=config('PG_SQL_PASSWORD')
        )
    except DatabaseError as ex:
        raise ex