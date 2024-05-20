from enum import Enum, unique

# -----


class NoValue(Enum):

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)

# ----

@unique
class TestsEventType(NoValue):
    VERIFIED_USER = 'VERIFIED_USER'
    FINISHED_ANALYZE = 'FINISHED_ANALYZE'
    FINISHED_TEST = 'FINISHED_TEST'


# -----

@unique
class UsersEventType(NoValue):
    DELETED = 'DELETED'
    CHANGED_WALLET_STATE = 'CHANGED_WALLET_STATE'
    NEW_USER = 'NEW_USER'
    UPDATED_INFO = 'UPDATED_INFO'
    NEW_VERIFICATION = 'NEW_VERIFICATION'