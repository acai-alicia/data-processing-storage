class InMemoryDB:
    def __init__(self):
        self.database = {}
        self.transaction = None
        self.transaction_active = False

    def get(self, key):
        if self.transaction_active and key in self.transaction:
            return self.transaction[key]
        return self.database.get(key, None)

    def put(self, key, val):
        if not self.transaction_active:
            raise Exception("No active transaction to put a value.")
        self.transaction[key] = val

    def begin_transaction(self):
        if self.transaction_active:
            raise Exception("Transaction already in progress.")
        self.transaction = {}
        self.transaction_active = True

    def commit(self):
        if not self.transaction_active:
            raise Exception("No active transaction to commit.")
        for key, val in self.transaction.items():
            self.database[key] = val
        self.transaction = None
        self.transaction_active = False

    def rollback(self):
        if not self.transaction_active:
            raise Exception("No active transaction to rollback.")
        self.transaction = None
        self.transaction_active = False
