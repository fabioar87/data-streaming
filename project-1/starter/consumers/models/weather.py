"""Contains functionality related to Weather"""
import logging
from enum import IntEnum

logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info(
            f"weather process_message - {message.key()}"
        )
        self.temperature = message.value()['temperature']
        self.status = message.value()['status']
