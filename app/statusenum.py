from enum import Enum

class Status(Enum):
    ONLINE = 1          # Server returned 200
    PROTECTED = 2       # Protected and able to log in with given username/password
    BROKEN = 3          # Couldn't connect
    LOGIN_FAILED = 4    # Invalid username/password
    NO_LOGIN = 5        # Expected basic auth but got plain HTTP
    UNAUTHORIZED = 6    # Expected plain HTTP but got basic auth
