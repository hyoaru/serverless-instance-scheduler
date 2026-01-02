from abc import ABC, abstractmethod

from app.services.ec2_instance_state_manager.interface import Ec2InstanceStateManagerABC


class Ec2InstanceStateActionStrategyABC(ABC):
    @abstractmethod
    def execute(self, manager: Ec2InstanceStateManagerABC):
        pass
