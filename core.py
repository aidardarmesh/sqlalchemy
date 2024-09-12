from sqlalchemy import text, insert

from db import engine, aengine
from models import metadata_obj, workers_table


def create_tables():
    engine.echo = False
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)
    engine.echo = True


def insert_data():
    with engine.connect() as conn:
        # stmt = """INSERT INTO workers (username) VALUES
        #         ('AO Bobr'),
        #         ('OOO Volk')
        #         """
        stmt = insert(workers_table).values(
            [
                {"username": "AO Bobr"},
                {"username": "OOO Volk"}
            ]
        )
        conn.execute(stmt)
        conn.commit()

