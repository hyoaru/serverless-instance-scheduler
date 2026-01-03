from abc import ABC

from botocore.client import BaseClient

from app.services.ec2_instance_state_manager.helper.commands.interface import Ec2InstanceStateManagerHelperCommandABC


class Ec2InstanceStateManagerHelperABC(ABC):
    client: BaseClient

    def __init__(self, client: BaseClient):
        pass

    def execute(self, command: Ec2InstanceStateManagerHelperCommandABC):
        pass
