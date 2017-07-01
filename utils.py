import json
import hashlib

def set_vars(self, args):
    for arg in args:
        setattr(self, arg, args[arg])

def get_hash(self):
    return hashlib.md5(str(self.__dict__).encode()).hexdigest()

def get_json(self):
    return json.dumps(self.__dict__)
