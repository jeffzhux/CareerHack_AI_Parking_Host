from typing import Optional
from pydantic import BaseModel


class Security_Guard(BaseModel):
    username : str
    password : str