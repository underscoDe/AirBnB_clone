#!usr/bin/python3
"""Contains the entry point of the command interpreter."""
import cmd
import re
from shlex import split

from models import storage
from models.user import User


def parse(arg):
    """
    Method written to take and parse input before use
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            rtl = [i.strip() for i in lexer]
            rtl.append(brackets.group())
            return rtl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        rtl = [i.strip() for i in lexer]
        rtl.append(curly_braces.group())
        return rtl


class HBNBCommand(cmd.Cmd):
    """HBnB Console.
    See https://docs.python.org/3/library/cmd.html\
        for more details

    Attr:
        custom_prompt (str): command line prompt
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User"
    }

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

    def do_create(self, arg):
        """
        Create instance of class
        """
        args = parse(arg)
        if len(args) == 0:
            print("** Class name  missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** Class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Show class + id
        """
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** Class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** Class doesn't exist**")
        elif len(args) == 1:
            print("** instance id doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
