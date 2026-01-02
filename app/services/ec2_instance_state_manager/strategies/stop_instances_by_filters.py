from typing import Any, cast

from app.services.ec2_instance_state_manager.helper import Ec2InstanceStateManagerHelper
from app.services.ec2_instance_state_manager.helper.commands import (
    GetInstancesByFilters,
    StopInstances,
)
from app.services.ec2_instance_state_manager.strategies.interface import (
    Ec2InstanceStateActionStrategyABC,
)
from app.utilities.logger import Logger

logger = Logger.get_instance()


class StopInstancesByFilters(Ec2InstanceStateActionStrategyABC):
    def execute(self, manager):
        helper = Ec2InstanceStateManagerHelper(manager.client)
        instances = cast(Any, helper.execute(GetInstancesByFilters(manager.filters)))
        ids = [x["InstanceId"] for x in instances["Reservations"][0]["Instances"]]
        return helper.execute(StopInstances(ids))
