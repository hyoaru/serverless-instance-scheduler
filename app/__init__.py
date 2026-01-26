import asyncio

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser

from app.models import Event
from app.services.office_hour_instances_state_manager import OfficeHourInstancesStateManager
from app.instances import logger


async def main(event: Event, context: LambdaContext):
    await OfficeHourInstancesStateManager().execute(event.action)
    return {"status": 200, "message": f"Successfully executed {event.action}"}


@event_parser(model=Event)
@logger.inject_lambda_context
def handler(event: Event, context: LambdaContext):
    asyncio.run(main(event, context))
