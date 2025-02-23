import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')


class DB_Config():

    path = os.getcwd()
    db_path = os.path.join(path, DB_NAME)
    db_uri = f'sqlite:///{db_path}?check_same_thread=False'

    ENV = 'local'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI_MS', db_uri)
