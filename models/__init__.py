#!/usr/bin/python3
"""Create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
