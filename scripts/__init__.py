import asyncio
import logging

from weather import start_web_server

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def web_server():
    start_web_server()
