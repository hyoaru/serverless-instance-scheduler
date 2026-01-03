from botocore.client import BaseClient

from app.services.ec2_instance_state_manager.helper.commands.interface import Ec2InstanceStateManagerHelperCommandABC
from app.services.ec2_instance_state_manager.helper.interface import Ec2InstanceStateManagerHelperABC

__all__ = ["Ec2InstanceStateManagerHelperABC", "Ec2InstanceStateManagerHelper"]


class Ec2InstanceStateManagerHelper(Ec2InstanceStateManagerHelperABC):
    client: BaseClient

    def __init__(self, client: BaseClient):
        self.client = client

    def execute(self, command: Ec2InstanceStateManagerHelperCommandABC):
        return command.execute(self)
