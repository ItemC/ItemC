
def convert_str_array_to_binary(array):
    output = b''
    for string in array:
        output += string.encode() + b',' 
    return output

def convert_str_array_to_object(binary):
    output = []
    string = ""
    for byte in binary:
        if chr(byte) == ',':
            output.append(string)
            string = ""
        else:
            string += chr(byte)
    return output

str_array = (convert_str_array_to_binary(['abc', 'def']))
print (convert_str_array_to_object(str_array))
