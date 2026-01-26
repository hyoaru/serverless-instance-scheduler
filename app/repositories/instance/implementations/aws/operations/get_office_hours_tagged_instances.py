from typing import List, cast

from types_boto3_ec2.type_defs import FilterTypeDef

from app.instances import logger
from app.utilities.aws_client.operations.get_ec2_instances import GetEc2Instances

from ....models.instance import Instance
from ....operation_interface import InstanceRepositoryOperationABC
from ...aws import AwsInstanceRepository


class GetOfficeHoursTaggedInstances(InstanceRepositoryOperationABC[List[Instance] | None]):
    async def execute(self, repository):
        if not isinstance(repository, AwsInstanceRepository):
            raise TypeError("Repository must be an instance of AwsInstanceRepository")

        repository = cast(AwsInstanceRepository, repository)

        filters: List[FilterTypeDef] = [{"Name": "tag:Schedule", "Values": ["office-hours"]}]
        result = await repository.aws_client.execute(GetEc2Instances(filters))

        if not (instances := result["Reservations"][0].get("Instances", [])):
            return None

        instance_ids = [i.get("InstanceId") for i in instances]
        logger.debug("Found office-hours tagged instances", extra={"instance_ids": instance_ids})

        return [Instance(id=id) for id in instance_ids if id]
