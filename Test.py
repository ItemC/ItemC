from utils import *
import uuid

class Test:
    encoding = [
        ("i", "inputs"),
        ("i", "outputs")
    ]
    def __init__(self, **kwargs):
        set_instance_variables(Test, kwargs)

    def getTransactionsBinary(self, array):
        output = b''
        for transaction in array:
            output += transaction.encode()
        return output

transactions = [uuid.uuid4().hex, uuid.uuid4().hex]
outputs = [ uuid.uuid4().hex]
test = Test(inputs=len(transactions), outputs=len(outputs))

headers = encode(test)
print(headers)
body = test.getTransactionsBinary(transactions)
print (body)

outputFile = headers + body
print (decode(Test, outputFile[len(Test.encoding)]))


