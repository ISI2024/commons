from pydantic import BaseModel
from commons.enums import TestsEventType
from typing import Optional


class ExaminationResult(BaseModel):
    fk_user: str
    analyzer: str
    id: int
    examination_date: str
    leukocytes: Optional[str] = None
    nitrite: Optional[str] = None
    urobilinogen: Optional[str] = None
    protein: Optional[str] = None
    ph: Optional[str] = None
    blood: Optional[str] = None
    specific_gravity: Optional[str] = None
    ascorbate: Optional[str] = None
    ketone: Optional[str] = None
    bilirubin: Optional[str] = None
    glucose: Optional[str] = None
    micro_albumin: Optional[str] = None


class VerifiedUser(BaseModel):
    login: str
    analyzer_code: str
    examination_id: int

class FinishedTest(BaseModel):
    email: str
    # result: ExaminationResult

class TestsEvent(BaseModel):
    kind: TestsEventType
    data: ExaminationResult | VerifiedUser | FinishedTest