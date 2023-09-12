from pydantic import BaseModel


class Part(BaseModel):
    manufacturer: str
    model: str
    category: str
    part_number: str
