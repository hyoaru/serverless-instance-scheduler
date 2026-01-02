import boto3

from app.services.ec2_instance_state_manager import Ec2InstanceStateManager
from app.utilities.logger import Logger

ec2 = boto3.client("ec2")


def handler(event, context):
    Logger.setup_logging(is_verbose=True)
    logger = Logger.get_instance()

    logger.info("Initializing parameters")
    fn = context.function_name
    environment = fn[0 : fn.find("-")]
    action = "STOP"

    logger.info(f"Executing {action} for environment: {environment}")
    Ec2InstanceStateManager(ec2, environment).execute(action)

    return {"status": 200}
