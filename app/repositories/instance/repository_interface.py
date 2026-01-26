from abc import ABC, abstractmethod
from typing import TypeVar

from .operation_interface import InstanceRepositoryOperationABC


T = TypeVar("T")


class InstanceRepositoryABC(ABC):
    @abstractmethod
    async def execute(self, operation: InstanceRepositoryOperationABC[T]) -> T:
        pass
