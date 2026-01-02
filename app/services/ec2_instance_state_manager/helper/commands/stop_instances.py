from typing import List

from app.services.ec2_instance_state_manager.helper.commands.interface import (
    Ec2InstanceStateManagerHelperCommandABC,
)
from app.utilities.logger import Logger

logger = Logger.get_instance()


class StopInstances(Ec2InstanceStateManagerHelperCommandABC):
    instance_ids: List[str]

    def __init__(self, instance_ids: List[str]):
        self.instance_ids = instance_ids

    def execute(self, helper):
        logger.debug(f"Stoping instances: {self.instance_ids}")
        helper.client.stop_instances(InstanceIds=self.instance_ids)
