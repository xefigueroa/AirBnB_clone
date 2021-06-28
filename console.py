#!/usr/bin/python3
"""
HBNB Console Program
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    prompt = '(hbnb)'

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ EOF command to handle EOF signal """
        print()
        return True

    def emptyline(self):
        """Method called when an empty line is entered in response to the prompt"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
