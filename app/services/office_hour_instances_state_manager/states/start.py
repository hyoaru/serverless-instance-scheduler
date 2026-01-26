from app.instances import logger
from app.repositories.instance.implementations.aws.operations import GetOfficeHoursTaggedInstances, StartInstances

from .interface import OfficeHourInstancesStateManagerStateABC


class Start(OfficeHourInstancesStateManagerStateABC[None]):
    async def execute(self, manager):
        instances = await manager._instance_repository.execute(GetOfficeHoursTaggedInstances())

        if not instances:
            logger.info("No instances found to start")
            return

        await manager._instance_repository.execute(StartInstances(instances))
