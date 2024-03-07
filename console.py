#!/usr/bin/env python3
"""Airbnb project -- hbnb console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt."""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """_EOF method to exit program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """execute nothing upon the recieve of empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
