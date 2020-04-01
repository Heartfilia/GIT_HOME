from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_MINA = 200   # WeChat mini program
    USER_WX = 201     # WeChat Official Account
