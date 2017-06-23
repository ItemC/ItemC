from struct import pack, unpack

"""
Format for network requests. Network requests use binary to transport and receive information.
"""

class Test:
    encoding = [("H", 'id_'),       # left: Type to be stored
                ("L", "amount"),    # right: name of instance variable 
                ("32s", "to"),
                ("32s", "from_"),
                ("128s", "message")]
             
    def __init__(self, **kargs):
        setInstanceVars(self, kargs)

    def __str__(self):
        return ("""
_id: {}
amount: {}
to: {}
from_: {}
message: {}
        """.format(self.id_, self.amount, self.to, self.from_, self.message))


#### Utility functions below that need to be put into their own files

def setInstanceVars(obj, arguments):
    for varname in arguments:
        setattr(obj, varname, arguments[varname])

def get_encoding_string(encoding):
    return ''.join(map(lambda x: x[0], encoding))

def encode(obj):
    args = map(lambda x: x.encode("utf8") if type(x) == str else x, [getattr(obj, x[1]) for x in obj.encoding])
    return pack(get_encoding_string(obj.encoding), *args)

def decode(Object, binary):
    unpacked = unpack(get_encoding_string(Object.encoding), binary)
    kargs = {} 
    for index, pval in enumerate(unpacked):
        kargs[Object.encoding[index][1]] = pval
    return Object(**kargs)


obj = Test(
        id_=123,
        amount=55,
        to="asdk123k1asd",
        from_="asdk3kk3k",
        message="Fuck Yeah"
      )


encoded = encode(obj)
print ("Encoded", encoded, '\n')
decoded = decode(Test, encoded)
print ("Decoded", decoded)


