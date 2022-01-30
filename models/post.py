from datetime import datetime
from sqlalchemy import Table, Column, String, Integer, DateTime, Boolean, Text, ForeignKey
from database.db import meta, engine

posts = Table(
    'post',
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("author_id", Integer, nullable=False),
    Column("title", String(255), nullable=False),
    Column("body", Text, nullable=False),
    Column("created_at", DateTime, default=datetime.now),
    Column("updated_at", DateTime, default=datetime.now, onupdate=datetime.now),
    Column("published_at", DateTime)
)

meta.create_all(engine)
