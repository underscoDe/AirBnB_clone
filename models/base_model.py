#!usr/bin/python3
"""Definition of the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initialize the BaseModel class.

        Args:
            self (BaseModel): the current instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
