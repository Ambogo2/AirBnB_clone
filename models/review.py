#!/usr/bin/python3
"""Module for reviews class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects."""

    place_id = ""
    user_id = ""
    text = ""
