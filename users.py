from pydantic import BaseModel
from test_service.common.enums import UsersEventType

class QrCodeData(BaseModel):
    login: str
    exp: int

class WalletChangeData(BaseModel):
    login: str
    change_amount: float


class UserData(BaseModel):
    email: str
    login: str
    wallet: float = 0.0

class UserVerification(BaseModel):
    email: str
    code: str

class UsersEvent(BaseModel):
    kind: UsersEventType
    data: UserData | UserVerification | WalletChangeData