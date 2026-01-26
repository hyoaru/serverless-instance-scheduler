from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from .repository_interface import InstanceRepositoryABC


T = TypeVar("T")


class InstanceRepositoryOperationABC(ABC, Generic[T]):
    @abstractmethod
    async def execute(self, repository: "InstanceRepositoryABC") -> T:
        pass
