from utils import *

class Test:
    encoding = [("i", '_id')]
    def __init__(self, **kwargs):
        set_instance_variables(Test, kwargs)

t = Test(_id=1)
print (encode(t))
