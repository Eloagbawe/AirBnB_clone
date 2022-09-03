#!/usr/bin/python3
"""The command prompt class - HBNBCommand"""


import cmd
from models import storage
import sys
import models
import re


classes = models.classes


def split_arg(arg):
    """splits cmd arguments"""
    if arg.count("\"") >= 1:
        arg_list = arg.split(" \"")[0].split(" ")
        quote_text = re.findall(r'"([^"]*)"', arg)
        arg_list.extend(quote_text)
    else:
        arg_list = arg.split(" ")
    return arg_list


def convert(val):
    """converts value to proper type"""
    constructors = [int, float, str]
    for c in constructors:
        try:
            return c(val)
        except ValueError:
            pass


def find_models(args):
    data = storage.all()
    data_list = []
    arg_list = split_arg(args)

    if len(args) == 0:
        for value in data.values():
            data_list.append(str(value))
    elif arg_list[0] not in classes:
        print("** class doesn't exist **")
        return
    else:
        for value in data.values():
            if value.__class__.__name__ == arg_list[0]:
                data_list.append(str(value))
    return data_list

# class _Wrapper:

#     def __init__(self, fd):
#         self.fd = fd

#     def readline(self, *args):
#         try:
#             return self.fd.readline(*args)
#         except KeyboardInterrupt:
#             print()
#             sys.exit(1)
#             # return '\n'


class HBNBCommand(cmd.Cmd):
    """The Command prompt Class"""

    prompt = "(hbnb) "

    def __init__(self):
        """Initialization"""
        cmd.Cmd.__init__(self)
        # cmd.Cmd.__init__(self, stdin=_Wrapper(sys.stdin))
        # self.use_rawinput = False

    def do_EOF(self, arg):
        """Quit console"""
        print("")
        return True

    def help_EOF(self, arg):
        """help EOF"""
        print("Quits the program")

    def emptyline(self):
        """empty line. Do nothing"""
        return False

    def do_quit(self, arg):
        """Quits the program"""
        # sys.exit(0)
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_create(self, args):
        """creates a new instance of BaseModel"""
        arg_list = split_arg(args)

        if len(args) == 0:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_model = classes[arg_list[0]]()
            # storage.new(new_model)
            storage.save()
            print(new_model.id)

    def help_create(self):
        print("creates a new instance of BaseModel")
        print("Usage: create classname")

    def do_show(self, args):
        """Prints the string representation of
        an instance based on the class name and id
        """
        arg_list = split_arg(args)

        if len(args) == 0:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) <= 1:
            print("** instance id missing **")
        else:
            data = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key in data:
                print(data[key])
            else:
                print("** no instance found **")

    def help_show(self):
        """prints help text for show"""
        print("Prints the string representation "
              "of an instance based on the class name and id")
        print("Usage: show classname id")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        arg_list = split_arg(args)

        if len(args) == 0:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) <= 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            data = storage.all()
            if key in data:
                storage.delete(key)
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self, args):
        """prints help text for destroy"""
        print("Deletes an instance based on the class name and id")
        print("Usage: destroy classname")

    def do_all(self, args):
        """Prints all string representation
        of all instances based or not on the class name
        """
        data_list = find_models(args)
        if data_list is not None:
            print(data_list)

    def help_all(self):
        """prints help text for all"""
        print("Prints all string representation of "
              "all instances based or not on the class name")
        print("Usage: all | all classname")

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        arg_list = split_arg(args)

        if len(args) == 0:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) <= 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            data = storage.all()
            if key in data:
                if len(arg_list) == 2:
                    print("** attribute name missing **")
                elif len(arg_list) == 3:
                    print("** value missing **")
                else:
                    storage.update(key, arg_list[2], convert(arg_list[3]))
                    model = data[key]
                    model.save()
                    # model_dict = data[key].to_dict()
                    # model_dict[arg_list[2]] = convert(arg_list[3])
                    # storage.delete(key)
                    # updated_model = classes[arg_list[0]](**model_dict)
                    # storage.new(updated_model)
                    # updated_model.save()
            else:
                print("** no instance found **")

    def help_update(self):
        """help text for update"""
        print("Updates an instance based on the "
              "class name and id by adding or updating attribute")
        print("Usage: update classname attribute value")

    # def onecmd(self, s):
    #     return cmd.Cmd.onecmd(self, s)

    def precmd(self, line):
        p = r"^(\w*)\.(\w+)(?:\(([^)]*)\))$"
        m = re.search(p, line)
        if not m:
            return line
        command = m.group(2) + " " + m.group(1) + " " + m.group(3)
        # self.onecmd(command)
        return command
        # return cmd.Cmd.precmd(self, line)

    def do_count(self, args):
        """retrieves the number of instances of a class"""
        if len(args) == 0:
            print("** class name missing **")
        else:
            data_list = find_models(args)
            if data_list is not None:
                print(len(data_list))

    def help_count(self):
        """help text for the count command"""
        print("retrieves the number of instances of a class")
        print("Usage: count classname")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
