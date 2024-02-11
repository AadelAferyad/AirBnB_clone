#!/usr/bin/python3
"""
this file is for the console (commande line intrepreter)
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re
import json


class HBNBCommand(cmd.Cmd):
    """
class for command interpreter
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": "BaseModel", "User": "User",
               "Place": "Place", "State": "State", "City": "City",
               "Amenity": "Amenity", "Review": "Review"}

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

    def default(self, line):
        """ this is defualt """
        args = line.split(".")
        pattern = r"(?<=\"|\").+([^\")])"
        if not line:
            return
        elif ".all()" in line and len(line) > 6:
            self.do_all(args[0])
        elif ".count()" in line and len(line) > 8:
            if not args[0] in HBNBCommand.classes:
                self.print_werror(2)
            else:
                count = 0
                dic = storage.all()
                for key, value in dic.items():
                    obj = dic[key].to_dict()
                    if obj["__class__"] == args[0]:
                        count += 1
                print(count)
        elif (((".show(" in line) and (")" in line)) or
              ((".destroy(" in line) and (")" in line))) and len(line) > 8:
            regex_id = ""
            full_cmd = ""
            matchs = re.search(pattern, args[1])
            if matchs:
                regex_id = matchs.group()
            full_cmd += args[0] + " " + regex_id
            if ("show" in line):
                self.do_show(full_cmd)
            else:
                self.do_destroy(full_cmd)
        elif ((".update(" in line) and (")" in line)) and len(line) > 8:
            full_pattern = r"(?<=\(|\").+([^\)])"
            full_cmd = ""
            regex_full = ""
            matchs = re.search(full_pattern, args[1])
            if matchs:
                regex_full = matchs.group()
            regex_id, regex_att, regex_va = regex_full.split(",")
            matchs = re.search(pattern, regex_id)
            if matchs:
                regex_id = matchs.group()
            if "\"" in regex_att:
                matchs = re.search(pattern, regex_att)
                if matchs:
                    regex_att = matchs.group()
            full_cmd += args[0] + " " + regex_id + " " + \
                regex_att + " " + regex_va
            print(full_cmd)
            self.do_update(full_cmd)
        else:
            super().default(line)

    def do_create(self, arg):
        """
create command to create new object and save it to Json file
        """
        if not arg:
            self.print_werror(1)
        elif arg not in HBNBCommand.classes:
            self.print_werror(2)
        elif arg in HBNBCommand.classes:
            instance = eval(HBNBCommand.classes[arg] + "()")
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
show command prints the string representation of an instance
        """
        args = arg.split()
        if not arg:
            self.print_werror(1)
        elif args[0] not in HBNBCommand.classes:
            self.print_werror(2)
        elif (len(args) < 2):
            self.print_werror(3)
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            if key not in dic:
                self.print_werror(4)
            else:
                obj = dic[key].to_dict()
                instance = eval(HBNBCommand.classes[args[0]] + "(**obj)")
                print(instance)

    @staticmethod
    def print_werror(case):
        """ this functions is for reapeted errors """
        if case == 1:
            print("** class name missing **")
        elif case == 2:
            print("** class doesn't exist **")
        elif case == 3:
            print("** instance id missing **")
        elif case == 4:
            print("** no instance found **")

    @staticmethod
    def all_formater(arg, i, key, **dic):
        all_instances = ""
        if i != 0:
            all_instances = all_instances + "\", \""
        instance = eval(HBNBCommand.classes[arg] + "(**dic)")
        all_instances = all_instances + str(instance)
        return all_instances

    def do_destroy(self, arg):
        """
destroy command Deletes an instance
        """
        args = arg.split()
        if not arg:
            self.print_werror(1)
        elif args[0] not in HBNBCommand.classes:
            self.print_werror(2)
        elif (len(args) < 2):
            self.print_werror(3)
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            if dic.pop(key, None) is None:
                self.print_werror(4)
            else:
                storage.save()

    def do_all(self, arg):
        """
all command prints all string representation of all instances
        """
        i = 0
        if arg and arg not in HBNBCommand.classes:
            self.print_werror(2)
            return 0
        dic = storage.all()
        fromat = "[\""
        for key, value in dic.items():
            clss = key.split(".")
            obj = value.to_dict()
            if arg:
                if clss[0] == arg:
                    fromat += self.all_formater(arg, i, key, **obj)
                    i += 1
            else:
                fromat += self.all_formater(clss[0], i, key, **obj)
                i += 1
        fromat = fromat + "\"]"
        print(fromat)

    def do_update(self, arg):
        """
update command updates an instance and save it to json file
        """
        args = arg.split()
        if not arg:
            self.print_werror(1)
        elif args[0] not in HBNBCommand.classes:
            self.print_werror(2)
        elif len(args) < 2:
            self.print_werror(3)
        else:
            dic = storage.all()
            key = args[0] + "." + args[1]
            if key not in dic:
                self.print_werror(4)
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = dic[key].to_dict()
                obj_key = args[2]
                if "\"" in obj_key:
                    obj_key = obj_key.replace("\"", "")
                obj[obj_key] = json.loads(args[3])
                instance = eval(HBNBCommand.classes[args[0]]+"(**obj)")
                storage.new(instance)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
