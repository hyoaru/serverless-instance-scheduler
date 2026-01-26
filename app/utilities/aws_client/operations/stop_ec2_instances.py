from types_boto3_ec2 import EC2Client

from app.instances import logger

from .interface import AwsClientOperationABC


class StopEc2Instances(AwsClientOperationABC[None]):
    instance_ids: list[str]

    def __init__(self, instance_ids: list[str]):
        self.instance_ids = instance_ids

    async def execute(self, client):
        ec2: EC2Client = client.session.client("ec2")
        logger.info("Stoping instances", extra={"ids": self.instance_ids})
        ec2.stop_instances(InstanceIds=self.instance_ids)
