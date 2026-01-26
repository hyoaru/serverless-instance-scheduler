from typing import Literal

from pydantic import BaseModel


class Event(BaseModel):
    action: Literal["START", "STOP"]
