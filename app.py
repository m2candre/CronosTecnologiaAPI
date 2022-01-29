from fastapi import FastAPI
from routes.user import user
from config.openapi import tags_metadata

app = FastAPI(
    title="Cronos API",
    description="REST API usando Python e PostgreSQL",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(user)
