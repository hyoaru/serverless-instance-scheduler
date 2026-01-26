from abc import ABC, abstractmethod
from typing import TypeVar

from boto3 import Session

from .operations.interface import AwsClientOperationABC
from .settings import Settings

T = TypeVar("T")


class AwsClientABC(ABC):
    session: Session
    _settings: Settings

    @abstractmethod
    async def execute(self, operation: AwsClientOperationABC[T]) -> T:
        pass
