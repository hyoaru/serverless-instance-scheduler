from typing import Any, Dict, List, Literal

from botocore.client import BaseClient


class Ec2InstanceStateManagerABC:
    client: BaseClient
    filters: List[Dict[str, Any]]

    def __init__(
        self,
        client: BaseClient,
        environment: Literal["dev", "stage", "prod"],
    ):
        pass

    def execute(self, strategy: str):
        pass
