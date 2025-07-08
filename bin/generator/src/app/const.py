import os
from dotenv import load_dotenv

load_dotenv()

WORKSPACE = os.getenv('WORKSPACE', "/app/mnt-workspace")