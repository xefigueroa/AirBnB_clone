#!/usr/bin/python3
"""
HBNB Console Program
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    prompt = '(hbnb)'
    cls = ['BaseModel', 'User', 'State',
           'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ EOF command to handle EOF signal """
        print()
        return True

    def emptyline(self):
        """
        Method called when an empty line is entered in
        response to the prompt
        """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        if len(args) == 0:
            print("** class name missing **")
        elif args in self.cls:
            new_inst = eval(args + "()")
            storage.new(new_inst)
            print(new_inst.id)
            storage.save()
        else:
            print("** class doesn't exists **")

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on class name and id
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.cls:
            print("** class doesn't exists **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            if key in dic:
                print(dic[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on class name and id """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.cls:
            print("** class doesn't exists **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            if key in dic:
                del dic[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
            Prints all string representation of all instances based or not
            on the class name
        """
        dic = storage.all()
        if len(args) == 0:
            for keys in dic:
                print(dic[keys])
        elif args in self.cls:
            for keys in dic:
                if args in keys:
                    print(dic[keys])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
            Updates an instance based on class name and id by adding or
            updating attribute.
            Usage: update <cls name> <id> <att name> "<att value>"
        """
        args = args.split()
        dic = storage.all()
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.cls:
            print("** class doesn't exists **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif key not in dic:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            for k, v in dic.items():
                if args[1] == v.id:
                    setattr(v, args[2], args[3])
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
