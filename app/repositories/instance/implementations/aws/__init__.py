from typing import Optional, TypeVar

from app.utilities.aws_client import AwsClient, AwsClientABC

from ...operation_interface import InstanceRepositoryOperationABC
from ...repository_interface import InstanceRepositoryABC
from .settings import Settings

T = TypeVar("T")


class AwsInstanceRepository(InstanceRepositoryABC):
    aws_client: AwsClientABC
    _settings: Settings

    def __init__(self, aws_client: Optional[AwsClientABC] = None, settings: Optional[Settings] = None) -> None:
        self.aws_client = aws_client or AwsClient()
        self._settings = settings or Settings()

    async def execute(self, operation: InstanceRepositoryOperationABC[T]) -> T:
        return await operation.execute(self)
