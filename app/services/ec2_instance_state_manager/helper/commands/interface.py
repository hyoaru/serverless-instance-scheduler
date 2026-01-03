from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.services.ec2_instance_state_manager.helper.interface import Ec2InstanceStateManagerHelperABC


class Ec2InstanceStateManagerHelperCommandABC(ABC):
    @abstractmethod
    def execute(self, helper: "Ec2InstanceStateManagerHelperABC"):
        pass
