# Author: Sakthi Santhosh
# Created on: 04/10/2023
from sqlalchemy.exc import OperationalError
from time import sleep

from lib import app_handle, db_handle
from lib.config import Config

def db_init():
    for _ in range(Config.RETRY_COUNT):
        try:
            with app_handle.app_context():
                db_handle.create_all()
            print("Info: Connection with database succeded.")
            break
        except OperationalError:
            print(f"Error: Connection to database failed.")
        except:
            print("Error: Something went wrong.")

        print(f"Info: Retrying in {Config.RETRY_DURATION} second(s).")
        sleep(Config.RETRY_DURATION)
    else:
        exit(1)
