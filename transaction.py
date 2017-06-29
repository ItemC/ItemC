class Transaction:
    encode = [
        ("32s", "id"),
        ("i", "usedTransactionsCount"),
        ()
    ]
    __init__():