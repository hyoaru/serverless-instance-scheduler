from typing import Literal, Type

from .interface import OfficeHourInstancesStateManagerStateABC
from .start import Start
from .stop import Stop


class OfficeHourInstancesStateManagerStateFactory:
    @staticmethod
    def create(action: Literal["START", "STOP"]) -> Type[OfficeHourInstancesStateManagerStateABC]:
        match action:
            case "START":
                return Start
            case "STOP":
                return Stop
