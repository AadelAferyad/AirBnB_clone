#!/usr/bin/python3
"""
this file is for the console (commande line intrepreter)
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class for command interpreter
    """
    classes = {"BaseModel": "BaseModel"}
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
            print("** class name missing **")
        elif arg in HBNBCommand.classes:
            # obj = getattr(class_module, arg)
            instance = eval(HBNBCommand.classes[arg]+"()")
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
Prints the string representation of an instance
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            if not key in dic:
                print("** no instance found **")
            else:
                instance = eval(HBNBCommand.classes[args[0]]+"(**dic[key])")
                print(instance)

    @staticmethod
    def print_werror(arg):
        """ this functions is for reapeted errors"""
        

    def do_destroy(self):
        """ """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
