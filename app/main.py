from typing import Optional
from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware
from db import DatabaseManager
from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str


app = FastAPI()
manager = DatabaseManager()


origins = [
    "http://localhost",
    "http://localhost:3000",  # Add the domain of your Next.js app here
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logging.basicConfig(level=logging.INFO)


@app.get("/api/posts")
async def get_posts():
    # Logic to retrieve all posts from the database
    # Return a list of Post objects
    posts_list = manager.get_posts()
    if len(posts_list) > 0:
        posts = []
        for post in posts_list:
            posts.append({"id": post[0], "title": post[1], "content": post[2]})
        return {"posts": posts}


@app.put("/api/posts")
async def update_post(post: Post):
    post = manager.update_post(post)
    if post is not None:
        return {"message": "Post updated successfully"}
    return {"message": "Post was not updated, please try again"}


@app.delete("/api/posts/{id}")
async def delete_post(id: int):
    postId = manager.delete_post(id)
    if postId is not None:
        return {"message": "Post deleted successfully", postId: postId}
    return {"message": "Post was not deleted, please try again"}


@app.post("/api/posts")
async def add_post(post: Post):
    postId = manager.add_post(post)
    post.id = postId
    return {"message": "Post added successfully", "post": post}


@app.get("/api/posts/{id}")
async def get_post(id: int):
    # Logic to retrieve a specific post by ID
    post = manager.get_post(id)
    if post is not None:
        return {"id": post[0], "title": post[1], "content": post[2]}
    # Return an error response if the post is not found
    return {"error": "Post not found"}


@app.get("/api/hp_data")
async def get_hp_data():
    # Logic to retrieve headline data for the homepage
    # Return a dict with the headline data
    return {"headline": "<h1>Welcome</h1>"}
