import uvicorn 
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.project_config import project_settings
from src.models import db_helper
from src.api.api_v1 import users_enpoint
from src.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    print("engine dispose")
    await db_helper.dispose()


application = FastAPI(
    lifespan=lifespan,
    title=project_settings.PROJECT_NAME,
    version=project_settings.VERSION,
)

application.include_router(users_enpoint.router)


if __name__ == "__main__":
    uvicorn.run("main:application", reload=True)
