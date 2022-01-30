from fastapi import FastAPI
from routes.user import user
from routes.post import post
from config.openapi import tags_metadata

app = FastAPI(
    title="Cronos API",
    description="REST API usando Python e PostgreSQL",
    version="0.0.2",
    openapi_tags=tags_metadata,
)

app.include_router(user)
app.include_router(post)
