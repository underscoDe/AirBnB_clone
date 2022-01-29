#!usr/bin/python3
"""Definition of the BaseModel class."""
import json


class FileStorage:
    """Serializes instances to a JSON file \
        and deserializes JSON file to instances.

        Args:
            __file_path (str): string - path to the JSON file
            __objects (dict): empty but will store \
                all objects by <class name>.id
    """
    # private instance attributes
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """Returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

