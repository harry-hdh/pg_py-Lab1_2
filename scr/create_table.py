import psycopg2
from config import load_config
def create_tables():
    """ Create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER  PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            url_key VARCHAR(1000) NOT NULL,
            description TEXT NULL,
            image_urls VARCHAR NULL
        )
        """

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                #for command in commands:
                cur.execute(command)

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
if __name__ == '__main__':
    create_tables()