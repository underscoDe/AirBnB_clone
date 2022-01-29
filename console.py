#!usr/bin/python3
"""Contains the entry point of the command interpreter."""
import cmd
from models.user import User

class HBNBCommand(cmd.Cmd):
    """HBnB Console.
    See https://docs.python.org/3/library/cmd.html\
        for more details

    Attr:
        custom_prompt (str): command line prompt
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Ignore empty lines + ENTER."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_exit(self, arg):
        """Exit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        # Go to a new line and before exiting
        print("")
        self.do_exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
