#!/usr/bin/python3
""" package """
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()