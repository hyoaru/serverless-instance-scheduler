from abc import ABC, abstractmethod

from app.services.ec2_instance_state_manager.helper.interface import (
    Ec2InstanceStateManagerHelperABC,
)


class Ec2InstanceStateManagerHelperCommandABC(ABC):
    @abstractmethod
    def execute(self, helper: Ec2InstanceStateManagerHelperABC):
        pass
