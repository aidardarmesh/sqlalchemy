from db import engine, aengine
from models import metadata_obj


def create_tables():
    metadata_obj.create_all(engine)

