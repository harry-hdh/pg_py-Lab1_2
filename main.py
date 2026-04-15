import psycopg2
import json
import glob
from psycopg2.extras import execute_values
from setuptools._distutils import command

from scr.config import load_config


def insert_data(file):
    with open(f"{file}", "r") as f:
        data_list = json.load(f)

    command = """INSERT INTO products(id, name, price, url_key, description, image_urls) VALUES (%s,%s,%s,%s,%s,%s)
                ON CONFLICT (id) DO NOTHING;"""

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # records = []
                for item in data_list:
                    # records.append((
                    #     item.get('id'),  # keep as int
                    #     item.get('name'),  # string
                    #     item.get('price'),  # number
                    #     item.get('url_key'),
                    #     item.get('description'),
                    #     json.dumps(item.get('image_urls'))  # only JSON field
                    # ))
                    cur.execute(command, (item.get('id'),
                                              item.get('name'),
                                              item.get('price'),
                                              item.get('url_key'),
                                              item.get('description'),
                                              json.dumps(item.get('image_urls'))
                                          )
                                )

                # execute_values(cur, command, records)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def get_json_file_name():
    filelist = []
    for file in glob.glob("/home/hdh/pg_py-Lab1_2/files/*.json"):
        filelist.append(file)
    return(filelist)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for f in get_json_file_name():
        print(f'Processing: {f}')
        insert_data(f)

