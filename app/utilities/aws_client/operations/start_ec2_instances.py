from types_boto3_ec2 import EC2Client

from app.instances import logger

from .interface import AwsClientOperationABC


class StartEc2Instances(AwsClientOperationABC[None]):
    instance_ids: list[str]

    def __init__(self, instance_ids: list[str]):
        self.instance_ids = instance_ids

    async def execute(self, client):
        ec2: EC2Client = client.session.client("ec2")
        logger.info("Starting instances", extra={"ids": self.instance_ids})
        ec2.start_instances(InstanceIds=self.instance_ids)
