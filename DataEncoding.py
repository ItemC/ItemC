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
        self.id_ = kargs['id_']
        self.amount = kargs['amount']
        self.to = kargs['to']
        self.from_ = kargs['from_']
        self.message = kargs['message']
            
    def __str__(self):
        return ("""
_id: {}
amount: {}
to: {}
from_: {}
message: {}
        """.format(self.id_, self.amount, self.to, self.from_, self.message))

def get_encoding_string(encoding):
    return ''.join(map(lambda x: x[0], encoding))


def encode(self):
    args = map(lambda x: x.encode("utf8") if type(x) == str else x, [getattr(self, x[1]) for x in self.encoding])

    return pack(get_encoding_string(Object.encoding), *args)

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
print (encoded)
decoded = decode(Test, encoded)
print (obj)


