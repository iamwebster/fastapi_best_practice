from dotenv import load_dotenv
from pydantic_settings import BaseSettings 

load_dotenv()


class MysqlSettings(BaseSettings):
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "root"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = "best_practice"
    DB_ECHO: bool = False
    
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    @property
    def database_url(self) -> str:
        return (
            f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )

    
db_settings = MysqlSettings()
