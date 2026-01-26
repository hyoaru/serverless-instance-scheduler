from app.instances import logger
from app.repositories.instance.implementations.aws.operations import GetOfficeHoursTaggedInstances, StopInstances

from .interface import OfficeHourInstancesStateManagerStateABC


class Stop(OfficeHourInstancesStateManagerStateABC[None]):
    async def execute(self, manager):
        instances = await manager._instance_repository.execute(GetOfficeHoursTaggedInstances())

        if not instances:
            logger.info("No instances found to stop")
            return

        await manager._instance_repository.execute(StopInstances(instances))
