from pydantic import BaseModel


class HealthCheck(BaseModel):
    work_status: bool = True
