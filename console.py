#!/usr/bin/python3
"""Module for HBNBCommand class."""

import cmd
import sys
import re
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = '(hbnb)'

    classes = [
                "BaseModel",
                "User",
                "Review",
                "City",
                "Place",
                "Amenity",
                "State"]

    def do_quit(self, line):
        """exits the program"""
        sys.exit()

    def d0_EOF(self, line):
        """exits the program"""
        print()
        sys.exit()

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}()")
            storage.save()
            print(new_instance.id)    #print instance of newly created instance
   
    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(line)

        if len(args):
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                del objects[key]   #delete the object
                storage.save()   #save changes in storage
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
        objects = storage.all()

        commands = shlex.split(line)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, line):
        """
        Counts and retrieves the number of instances of a class
        """
        objects = storage.all()

        commands = shlex.split(line)

        if line:
            cls_nm = commands[0]

        count = 0

        if commands:
            if cls_nm in self.classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == cls_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()