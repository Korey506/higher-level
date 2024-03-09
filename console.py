#!/usr/bin/env python3
"""Airbnb project -- hbnb console"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt."""
    prompt = "(hbnb) "
    lst_classes = ['BaseModel']

    def do_EOF(self, line):
        """_EOF method to exit program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """execute nothing upon the recieve of empty line"""
        pass

    def do_create(self, type_model):
        """ Creates an instance according to a given class """

        if not type_model:
            print("** class name missing **")
        elif type_model not in self.lst_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Shows string representation of an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in self.lst_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in self.lst_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in self.lst_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [str(value)]
            print(list_instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

        args = arg.split(' ')
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.lst_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            found = False
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    setattr(value, args[2], args[3].strip('"'))
                    value.save()
                    found = True
                    break
            if not found:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

