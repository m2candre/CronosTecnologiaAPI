from enum import unique
from sqlalchemy import Table, Column, String, Integer, DateTime, Boolean, func
from database.db import meta, engine

users = Table(
    'user',
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), unique=True, nullable=False),
    Column("password", String(255), nullable=False),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
    Column("is_admin", Boolean, nullable=False, default=False)
)

meta.create_all(engine)
