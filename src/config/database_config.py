from typing import Optional

from pydantic import MySQLDsn
from dotenv import load_dotenv
from pydantic_settings import BaseSettings 

load_dotenv()


class MysqlSettings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DB: str
    DB_ECHO: bool = False

    @property
    def database_url(self) -> Optional[MySQLDsn]:
        return (
            f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )

    
mysql_settings = MysqlSettings()
