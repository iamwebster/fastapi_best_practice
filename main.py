import uvicorn 
from fastapi import FastAPI

from src.config.project_config import project_settings


app = FastAPI(
    title=project_settings.PROJECT_NAME,
    version=project_settings.VERSION,
    debug=project_settings.DEBUG
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
