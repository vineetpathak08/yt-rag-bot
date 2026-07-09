"""
Entrypoint. Run with: python main.py
"""
import logging

import uvicorn

from config.settings import settings
from api.app import app

settings.validate()
uvicorn.run(app, host=settings.server_name, port=settings.server_port)
