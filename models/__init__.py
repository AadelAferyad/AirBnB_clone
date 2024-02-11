#!/usr/bin/python3
""" this file is for the main package """


from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
