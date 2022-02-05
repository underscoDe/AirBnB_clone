#!usr/bin/python3
"""Definition of the BaseModel class."""
import json
from models.base_model import BaseModel
from models.user import User


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

    def save(self):
        """Serializes __objects to the JSON file"""
        objects_copy = FileStorage.__objects
        objects_dict = {
            obj: objects_copy[obj].to_dict() for obj in objects_copy.keys()
        }

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects \
            or do nothing whether the JSON file exists or not."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_dict = json.load(f)
                for obj in objects_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
