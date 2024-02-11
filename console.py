#!/usr/bin/python3
"""
    The hbnb console
    Console module for the command interpreter
"""

import cmd
import models
import shlex
import re
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Returns empty when there's no input
        """
        return

    def __validate_class(self, line):
        """to vaidate the class input in line"""
        class_name = self.parseline(line)[0]

        if class_name is None:
            print("** class name missing **")
            return None
        elif not globals().get(class_name):
            print(f"** class doesn't exist **")
            return None
        else:
            return True

    def __validate_id(self, line):
        """to validate the id input in line"""
        classname = self.parseline(line)[0]
        _id = self.parseline(line)[1]
        if _id.startswith('"') and _id.endswith('"'):
            _id = _id[1:-1]
        inst_data = models.storage.all().get(classname + '.' + _id)

        if not _id:
            print("** instance id missing **")
            return None
        elif inst_data is None:
            print("** no instance found **")
            return None
        else:
            return True, inst_data

    def do_create(self, line):
        """Create a new instance of BaseModel, save and print its id"""
        classname = self.parseline(line)[0]

        if not self.__validate_class(line):
            return
        new_instance = globals()[classname]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string rep of the instance based on passed id"""
        if not self.__validate_class(line):
            return

        result = self.__validate_id(line)
        if result:
            state, inst_data = result
            print(inst_data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not self.__validate_class(line):
            return

        result = self.__validate_id(line)
        if result:
            state, inst_data = result
            key = f"{inst_data.__class__.__name__}.{inst_data.id}"
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
based on or not on the class"""
        class_name = self.parseline(line)[0]

        if class_name and not globals().get(class_name):
            print("** class doesn't exist **")
        else:
            all_objs = models.storage.all()

            if class_name:
                keys = all_objs.keys()
                print([str(all_objs[key])
                      for key in keys if key.startswith(class_name)])
            else:
                for obj in all_objs:
                    print([str(all_objs[obj])])

    def do_update(self, line):
        """Updates an instance attribute based on the class name"""
        args = shlex.split(line)
        arg_count = len(args)

        if arg_count == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif arg_count == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif arg_count == 2:
                print("** attribute name missing **")
            elif arg_count == 3:
                print("** value missing **")
            else:
                if '{' in args[2]:
                    dict_arg = re.split(r" (?![^{}[\]()]*[}\]])", line)
                    for key, value in eval(dict_arg[2]).items():
                        argument = f"{args[0]} {args[1]} {key} {value}"
                        self.do_update(argument)
                else:
                    attr, value = args[2:4]
                    attr_type = type(value)
                    setattr(inst_data, attr, attr_type(value))
                    setattr(inst_data, 'updated_at', datetime.now())
                    models.storage.save()

    def __parse(self, arg_str):
        parsed_arg = re.split(r"\(|, (?![^{}[\]()]*[}\]])", arg_str[:-1])
        return parsed_arg

    def do_count(self, line):
        'Retrieves the number of instances of a class'
        if not self.__validate_class(line):
            return

        classname = self.parseline(line)[0]
        models.storage.reload()
        objects = models.storage.all()
        instances = [obj for obj in objects.values()
                     if type(obj).__name__ == classname]
        print(len(instances))

    def precmd(self, args):
        if "." in args:
            args = args.split('.', 1)
            classname = args[0]
            arguments = self.__parse(args[1])
            function = arguments[0]
            line = f"{function} {classname} {(' ').join(arguments[1:])}"
            return cmd.Cmd.precmd(self, line)
        else:
            return cmd.Cmd.precmd(self, args)
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
