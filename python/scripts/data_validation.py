from typing import Optional

import pydantic as py
import datetime

class User(py.BaseModel):
    first_name: str
    last_name: str
    age: int
    is_admin: bool=False
    birthday: Optional[datetime.date]=None

u1 = {
    "first_name": "Ferdinand",
    "last_name": "Steenkamp",
    "age": 28,
    "is_admin": True,
    "birthday": "2025-01-01"
}

u2 = {
    "first_name": "Stefan",
    "last_name": "Gerber",
    "age": 29,
    "is_admin": False,
    "birthday": "2025-01-01"
}

u1_validated = User.model_validate(u1)
u2_validated = User.model_validate(u2)

print(u1)
print(u2)
