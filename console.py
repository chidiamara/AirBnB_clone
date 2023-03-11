#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ cmd class """
    classes = ["BaseModel"]
    def main():
        """ main function """
        do_EOF(self, arg)
        do_quit(self, arg)
        emptyline(self)

    if sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)\n'

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        quit()
        return True

    def emptyline(self):
        """ do nothing when an empty line is entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
