# Author: Sakthi Santhosh
# Created on: 25/08/2023
from os import getenv
from secrets import token_hex

class Config:
    SECRET_KEY = token_hex(16)

    POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{POSTGRES_PASSWORD}@postgres/postgres"

    RETRY_COUNT = 30
    RETRY_DURATION = 5
