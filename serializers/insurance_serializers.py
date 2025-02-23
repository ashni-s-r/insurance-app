from typing import Optional

from pydantic import BaseModel


class InsuranceBase(BaseModel):
    name: str
    type: str
    premium: Optional[str]
    coverage: Optional[str]


class InsuranceCreate(InsuranceBase):
    pass


class InsuranceUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]
    premium: Optional[str]
    coverage: Optional[str]


class InsuranceResponse(InsuranceBase):
    id: int

    class Config:
        from_attributes = True
