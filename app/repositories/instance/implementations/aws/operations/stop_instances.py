from typing import List, cast

from app.utilities.aws_client.operations.stop_ec2_instances import StopEc2Instances

from ....models.instance import Instance
from ....operation_interface import InstanceRepositoryOperationABC
from ...aws import AwsInstanceRepository


class StopInstances(InstanceRepositoryOperationABC[List[Instance] | None]):
    instances: List[Instance]

    def __init__(self, instances: List[Instance]):
        self.instances = instances

    async def execute(self, repository):
        if not isinstance(repository, AwsInstanceRepository):
            raise TypeError("Repository must be an instance of AwsInstanceRepository")

        repository = cast(AwsInstanceRepository, repository)
        await repository.aws_client.execute(StopEc2Instances([i.id for i in self.instances]))
