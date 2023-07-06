import time

from pydantic import BaseModel


class ServerTime(BaseModel):
    server_time: int = 1688596630786
