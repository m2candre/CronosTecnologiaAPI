from os import getenv, environ
from sqlalchemy import create_engine, MetaData

engine = create_engine('postgresql+psycopg2://admin:admin@localhost/cronos_db') 
meta = MetaData()
conn = engine.connect()
