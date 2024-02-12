#!/usr/bin/python3
"""
instance for FileStorage
its reload the data from the JSON file into the storage
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
