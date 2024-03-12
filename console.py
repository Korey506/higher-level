#!/usr/bin/env python3
"""Airbnb project -- hbnb console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt."""
    prompt = "(hbnb) "
    lst_classes = [
            'BaseModel',
            'User',
            'State',
            'City',
            'Amenity',
            'Place',
            'Review'
            ]

    def do_EOF(self, line):
        """_EOF method to exit program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """execute nothing upon the recieve of empty line"""
        pass

    def do_create(self, type_model):
        """ Creates an instance according to a given class """

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        else:
            dct = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
                    }
            my_model = dct[type_model]()
            print(my_model.id)
            storage.save()

    def do_show(self, arg):
        """ Shows string representation of an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.lst_classes:
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

        if args[0] not in HBNBCommand.lst_classes:
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

        if args[0] not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == arg:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
            return
        a = ""
        for argv in arg.split(','):
            a = a + argv
        args = shlex.split(a)
        if args[0] not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_count(self, arg):
        """ prints the number of instances of a given class """
        class_name = arg.split('.')[0]
        if class_name not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
            return
        count = 0
        all_objs = storage.all()
        for key, value in all_objs.items():
            ob_name = value.__class__.__name__
            if ob_name == class_name:
                count += 1
        print(count)

    def do_show(self, arg):
        """ string rep of an instance based on id """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        class_name = args[0]

        if class_name not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]

        if not (instance_id.startswith('"') and instance_id.endswith('"')):
            print("** no instance found **")
            return

        instance_id = instance_id.strip('"')
        all_objs = storage.all()

        for key, value in all_objs.items():
            if value.id == instance_id and value.__class__.__name__ == class_name:
                print(value)
                return
        print("** no instance found **")

    def default(self, line):
        """
        Default method to handle unknown commands.
        """
        split_line = line.split('.')
        if len(split_line) == 2:
            class_name = split_line[0]
            action, identifier = split_line[1].split('(')
            identifier = identifier.strip(')')

            if action == 'all':
                if class_name in HBNBCommand.lst_classes:
                    self.do_all(class_name)
                else:
                    print("** class doesn't exist **")
            elif action == 'count':
                if class_name in HBNBCommand.lst_classes:
                    self.do_count(class_name)
                else:
                    print("** class doesn't exist **")
            elif action == 'show':
                if class_name in HBNBCommand.lst_classes:
                    self.do_show("{} {}".format(class_name, identifier))
                else:
                    print("** class doesn't exist **")
            elif action == 'destroy':
                if class_name in HBNBCommand.lst_classes:
                    self.do_destroy("{} {}".format(class_name, identifier))
                else:
                    print("** class doesn't exist **")
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
