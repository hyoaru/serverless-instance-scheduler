from typing import Literal, Optional

from app.repositories.instance.implementations.aws import AwsInstanceRepository
from app.repositories.instance.repository_interface import InstanceRepositoryABC

from .interface import OfficeHourInstancesStateManagerABC
from .states.factory import OfficeHourInstancesStateManagerStateFactory

__all__ = ["OfficeHourInstancesStateManager", "OfficeHourInstancesStateManagerABC"]


class OfficeHourInstancesStateManager(OfficeHourInstancesStateManagerABC):
    _instance_repository: InstanceRepositoryABC

    def __init__(self, instance_repository: Optional[InstanceRepositoryABC] = None):
        self._instance_repository = instance_repository or AwsInstanceRepository()

    async def execute(self, strategy: Literal["START", "STOP"]):
        state_class = OfficeHourInstancesStateManagerStateFactory.create(strategy)
        await state_class().execute(self)
