#!/usr/bin/python3
"""Module Review .."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class for representing reviews with public attributes.
    """
    place_id = ""
    user_id = ""
    text = ""
