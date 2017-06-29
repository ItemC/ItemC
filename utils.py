from struct import *

def set_instance_variables(obj, arguments):
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

def convert_array_to_binary(array, dataType):
    if dataType == str:
        return bytearray(map(lambda x: ord(x),  array))
    elif dataType == int:
        return bytearray(array)
    else:
        raise Exception("Invalid Type: {} not supported".format(dataType))
