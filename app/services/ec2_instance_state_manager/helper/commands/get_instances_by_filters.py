from typing import Any, Dict, List

from app.services.ec2_instance_state_manager.helper.commands.interface import (
    Ec2InstanceStateManagerHelperCommandABC,
)
from app.utilities.logger import Logger

logger = Logger.get_instance()


class GetInstancesByFilters(Ec2InstanceStateManagerHelperCommandABC):
    filters: List[Dict[str, List[Any]]]

    def __init__(self, filters: List[Dict[str, List[Any]]]):
        self.filters = filters

    def execute(self, helper):
        logger.debug("Getting instances by filters", extra={"filters": self.filters})
        return helper.client.describe_instances(Filters=self.filters)
