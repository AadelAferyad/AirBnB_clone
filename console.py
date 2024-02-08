#!/usr/bin/python3
"""
this file is for the console (commande line intrepreter)
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class for command interpreter
    """
    classes = {"BaseModel": "BaseModel", "User":"User"}
    def __init__(self):
        """ the constractor """
        super().__init__()
        self.prompt = "(hbnb) "

    def do_help(self, arg):
        """
help command to get informations about commands (help + command)
        """
        super().do_help(arg)

    def do_EOF(self, line):
        """
EOF command to exit the program or (CRTL + D)
        """
        return True

    def do_quit(self, line):
        """
Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
emptyline command to skip (if empty line passed as a command do nothing)
        """
        pass

    def do_create(self, arg):
        """
create command to create new object and save it to Json file
        """
        if not arg:
            self.print_werror(1)
        elif not arg in HBNBCommand.classes:
            self.print_werror(2)
        elif arg in HBNBCommand.classes:
            # obj = getattr(class_module, arg)
            instance = eval(HBNBCommand.classes[arg]+"()")
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
show command prints the string representation of an instance
        """
        args = arg.split()
        if not arg:
            self.print_werror(1)
        elif not args[0] in HBNBCommand.classes:
            self.print_werror(2)
        elif (len(args) < 2):
            self.print_werror(3)
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            if not key in dic:
                self.print_werror(4)
            else:
                instance = eval(HBNBCommand.classes[args[0]]+"(**dic[key])")
                print(instance)

    @staticmethod
    def print_werror(case):
        """ this functions is for reapeted errors"""
        if case == 1:
            print("** class name missing **")
        elif case == 2:
            print("** class doesn't exist **")
        elif case == 3:
            print("** instance id missing **")
        elif case == 4:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
destroy command Deletes an instance
        """
        args = arg.split()
        if not arg:
            self.print_werror(1)
        elif not args[0] in HBNBCommand.classes:
            self.print_werror(2)
        elif (len(args) < 2):
            self.print_werror(3)
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            # if not key in dic:
                # self.print_werror(4)
            if dic.pop(key, None) is None:
                self.print_werror(4)
            else:
                storage.save()

    def do_all(self, arg):
        """
all command prints all string representation of all instances
        """
        i = 0
        if arg:
            if not arg in HBNBCommand.classes:
                self.print_werror(2)
                return 0
        all_instances = "[\""
        dic = storage.all()
        for key, value in dic.items():
            key_class = key.split(".")
            if arg:
                if key_class[0] == arg:
                    if i != 0:
                        all_instances = all_instances + "\", \""
                    instance = eval(HBNBCommand.classes[arg] + "(**dic[key])")
                    all_instances = all_instances + str(instance)
                    i += 1
            else:
                if i != 0:
                        all_instances = all_instances + "\", \""
                instance = eval(HBNBCommand.classes[key_class[0]] + "(**dic[key])")
                all_instances = all_instances + str(instance)
                i += 1
        all_instances = all_instances + "\"]"
        print(all_instances)

    def do_update(self, arg):
        """
update command updates an instance and save it to json file
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()