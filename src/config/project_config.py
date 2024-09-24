from dotenv import load_dotenv 
from pydantic_settings import BaseSettings

load_dotenv()


class ProjectSettings(BaseSettings):
    PROJECT_NAME: str 
    VERSION: str 
    DEBUG: bool



project_settings = ProjectSettings()
