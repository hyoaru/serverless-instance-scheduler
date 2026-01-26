from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from ..interface import OfficeHourInstancesStateManagerABC


T = TypeVar("T")


class OfficeHourInstancesStateManagerStateABC(ABC, Generic[T]):
    @abstractmethod
    async def execute(self, manager: "OfficeHourInstancesStateManagerABC") -> T:
        pass
