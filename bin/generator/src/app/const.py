"""Shared configuration values for the generator app."""

import os
from dotenv import load_dotenv

load_dotenv()

WORKSPACE = os.getenv('WORKSPACE', "/app/mnt-workspace")
