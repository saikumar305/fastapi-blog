from fastapi import FastAPI
from routers.blog_routes import router as blog_router
from routers.user_routes import router as user_router

app = FastAPI()

app.include_router(blog_router, prefix="/blog", tags=["blog"])
app.include_router(user_router, prefix="/users", tags=["users"])