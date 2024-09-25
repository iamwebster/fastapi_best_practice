import uvicorn 
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.project_config import project_settings
from src.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("engine dispose")
    await db_helper.dispose()


application = FastAPI(
    lifespan=lifespan,
    title=project_settings.PROJECT_NAME,
    version=project_settings.VERSION,
)


if __name__ == "__main__":
    uvicorn.run("main:application", reload=True)
