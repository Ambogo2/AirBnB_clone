#!/usr/bin/python3
"""module for initialzing the package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
