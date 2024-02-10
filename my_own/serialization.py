#!/usr/bin/python3
import json
import os


class Base:
    """ basic class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def load_from_json(file):
        """ load from a file json"""
        if not os.path.exists(file):
            return (None)
        with open(file, 'r', encoding="utf-8") as fd:
            return (json.loads(fd.read()))

    def save_to_json(file, list_obj):
        with open(file, 'w', encoding="utf-8") as fd:
            fd.write(json.dumps(list_obj))

    def to_dic(self):
        """ converte a inctence to list of dictionaries"""
        return ({"firt_name" : self.first_name, "last_name" : self.last_name, "age" : self.age})

    @classmethod
    def serialization(cls, obj):
        st = []
        # st.append(obj.to_dic())
        if os.path.exists("file.json"):
            st = cls.load_from_json("file.json")
        st.append(obj.to_dic())
        cls.save_to_json("file.json", st)



a = Base("aadel", "Aa", 22)
a.serialization(a)
ls = []
ls = Base.load_from_json("file.json")

print(a.__dict__)
di = dict(a.__dict__)
print(di['first_name'])