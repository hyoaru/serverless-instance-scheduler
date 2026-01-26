from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from ..interface import AwsClientABC


T = TypeVar("T")


class AwsClientOperationABC(ABC, Generic[T]):
    @abstractmethod
    async def execute(self, client: "AwsClientABC") -> T:
        pass
