from Transaction import Transaction
import pprint

transactionData = {
    "inputs":[
        "1d98cab141b92c9846d4bc9b8a978d05d47845a7"
    ],
    "outputs":[
        {
            "toAddress":"MEgCQQDIU3aoetkliLVozO19waTQOTkrLsSSRoUi47YZZbGG1ByteGuDAXNdBNztxO68IqmeLTmOryGATtCPh7cz8dUjAgMBAAE=",
            "amount":25
        }
    ]
}


trans = Transaction(**transactionData)
trans.sign_transaction()
pprint.pprint(trans.send())
#print (trans.send())
