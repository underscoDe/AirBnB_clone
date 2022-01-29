#!usr/bin/python3
"""Contains the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBnB Console.
    See https://docs.python.org/3/library/cmd.html\
        for more details

    Attr:
        custom_prompt (str): command line prompt
    """
    custom_prompt = "(hbnb)"

    def emptyline(self):
        pass
