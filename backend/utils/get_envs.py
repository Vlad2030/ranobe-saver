import os
import typing

import dotenv


class Environs:
    def __init__(self) -> None:
        self.envs = dotenv.load_dotenv()

    @staticmethod
    def get(var: str) -> typing.Union[str, None]:
        dotenv.load_dotenv()
        return os.getenv(key=var)