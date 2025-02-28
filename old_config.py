import os
from typing import Literal

KEY= 'asdlajsdasASDASD'
ALGORITHM='HS256'

SMTP_HOST= 'smtp.gmail.com'
SMTP_PORT= 465
SMTP_USER= 'airstarview@gmail.com'
SMTP_PASS='guma lbnl pmgc uhqc'

MODE: Literal['DEV', 'TEST', 'PROD'] = os.getenv('MODE', 'DEV')