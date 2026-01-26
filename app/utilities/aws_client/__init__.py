from typing import Optional, TypeVar

from boto3 import Session

from .interface import AwsClientABC
from .operations.interface import AwsClientOperationABC
from .settings import Settings

T = TypeVar("T")

__all__ = ["AwsClient", "AwsClientABC", "Settings"]


class AwsClient(AwsClientABC):
    session: Session
    _settings: Settings

    def __init__(
        self,
        session: Optional[Session] = None,
        settings: Optional[Settings] = None,
    ):
        self._settings = settings or Settings()
        self.session = session or Session(region_name=self._settings.AWS_REGION)

    async def execute(self, operation: AwsClientOperationABC[T]) -> T:
        return await operation.execute(self)
