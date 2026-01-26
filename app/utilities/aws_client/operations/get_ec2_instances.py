from typing import List, Optional

from types_boto3_ec2 import EC2Client
from types_boto3_ec2.type_defs import DescribeInstancesResultTypeDef, FilterTypeDef

from app.instances import logger

from .interface import AwsClientOperationABC


class GetEc2Instances(AwsClientOperationABC[DescribeInstancesResultTypeDef]):
    filters: Optional[List[FilterTypeDef]]

    def __init__(self, filters: Optional[List[FilterTypeDef]]):
        self.filters = filters

    async def execute(self, client):
        ec2: EC2Client = client.session.client("ec2")

        if not self.filters:
            logger.info("Getting instances")
            return ec2.describe_instances()

        logger.info("Getting instances by filters", extra={"filters": self.filters})
        return ec2.describe_instances(Filters=self.filters)
