from turtle import title
from fastapi import APIRouter
from database.db import conn
from models.post import posts
from schemas.post import Post
from typing import List

from starlette.status import HTTP_204_NO_CONTENT

post = APIRouter()

@post.get("/posts/", tags=["posts"], response_model=List[Post], description="Get a list of all Posts")
def get_posts():
    return conn.execute(posts.select()).fetchall()


@post.get("/posts/{id}", tags=["posts"], response_model=Post, description="Get a single Post by Id")
def get_post(id: str):
    return conn.execute(posts.select().where(posts.c.id == id)).first()


@post.post("/posts/", tags=["posts"], response_model=Post, description="Create a new Post")
def create_post(post: Post):
    new_post = {"author_id": post.author_id, "title": post.title, "body": post.body} 
    result = conn.execute(posts.insert().values(new_post))
    return conn.execute(posts.select().where(posts.c.id == result.lastrowid)).first()


@post.put("/posts/{id}", tags=["posts"], response_model=Post, description="Update a Post by Id")
def update_post(post: Post, id: int):
    conn.execute(
        posts.update()
        .values(author_id=post.author_id, title=post.title, body=post.body)
        .where(posts.c.id == id)
    )
    return conn.execute(posts.select().where(posts.c.id == id)).first()


@post.delete("/posts/{id}", tags=["posts"], status_code=HTTP_204_NO_CONTENT)
def delete_post(id: int):
    conn.execute(posts.delete().where(posts.c.id == id))
    return conn.execute(posts.select().where(posts.c.id == id)).first()
