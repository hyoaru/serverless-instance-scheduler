from typing import Literal
from app.repositories.instance.repository_interface import InstanceRepositoryABC


class OfficeHourInstancesStateManagerABC:
    _instance_repository: InstanceRepositoryABC

    async def execute(self, strategy: Literal["START", "STOP"]):
        pass
