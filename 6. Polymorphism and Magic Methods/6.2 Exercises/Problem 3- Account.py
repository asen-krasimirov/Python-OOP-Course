

class Account:
    owner: str
    amount: int
    _transactions: list

    def __init__(self, owner: str, amount: int=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self._transactions.append(amount)

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: 'Account', amount_to_add: int):

        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")

        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __add__(self, other):
        new_account = Account(f'{self.owner}&{other.owner}', self.amount+other.amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account


def main():
    def add_transaction_test():
        acc = Account('owner1', 100)
        acc.add_transaction(100)
        assert acc.balance == 200, acc.balance
        print('add_transaction_test Test passed')

    def wrong_type_transaction_check():
        acc = Account('owner1', 100)
        acc.add_transaction('100')
        assert acc.balance == 200, acc.balance
        print('wrong_type_transaction_check Test passed')

    def validate_transaction_check():
        acc = Account('owner1', 100)
        Account.validate_transaction(acc, 100)
        assert acc.balance == 200, acc.balance
        print('validate_transaction_check Test passed')

    def wrong_validate_transaction_check():
        acc = Account('owner1', 100)
        Account.validate_transaction(acc, -101)

    def str_method_test():
        acc = Account('owner1')
        assert str(acc) == 'Account of owner1 with starting amount: 0', acc
        print('str_method_test Test passed')

    def repr_method_test():
        acc = Account('owner1')
        assert repr(acc), 'Account(owner1, 0)'
        print('repr_method_test Test passed')

    def balance_test():
        acc = Account('owner1', 10)
        acc.add_transaction(100)
        assert acc.balance == 110, f'acc balance: {acc.balance}'
        print('balance_test Test passed')

    def len_method_test():
        acc = Account('owner1', 100)
        acc.add_transaction(100)
        acc.add_transaction(200)
        acc.add_transaction(300)
        assert len(acc) == 3, len(acc)
        print('len_method_test Test passed')

    def iter_test():
        print('iter_test:')
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        for transaction in acc:
            print(transaction)
        print('test completed')

    def getitem_method_test():
        acc = Account('owner1', 100)
        acc.add_transaction(100)
        acc.add_transaction(200)
        assert acc[1] == 200, acc[1]
        print('getitem_method_test Test passed')

    def reversed_method_test():
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        assert list(reversed(acc)) == [30, -20, 20], list(reversed(acc))
        print('reversed_method_test Test passed')

    def comparison_tests():
        acc1 = Account('bob', 10)
        acc2 = Account('john')
        acc1.add_transaction(20)
        acc1.add_transaction(-20)
        acc1.add_transaction(30)
        acc2.add_transaction(10)
        acc2.add_transaction(60)

        assert (acc1 > acc2) is False
        assert (acc1 >= acc2) is False
        assert (acc1 < acc2) is True
        assert (acc1 <= acc2) is True
        assert (acc1 == acc2) is False
        assert (acc1 != acc2) is True
        print('comparison_tests Test passed')

    def account_addition_test():
        acc1 = Account('bob', 10)
        acc2 = Account('john')
        acc3 = acc1 + acc2
        assert acc3.owner == 'bob&john', acc3.owner
        assert acc3.amount == 10, acc3.amount
        assert str(acc3) == 'Account of bob&john with starting amount: 10'
        print('account_addition_test Test passed')

    def account_addition_transactions_test():
        acc1 = Account('bob', 10)
        acc2 = Account('john')
        acc1.add_transaction(20)
        acc1.add_transaction(-20)
        acc1.add_transaction(30)
        acc2.add_transaction(10)
        acc2.add_transaction(60)
        acc3 = acc1+acc2
        assert acc3._transactions == [20, -20, 30, 10, 60], acc3._transactions
        print('account_addition_transactions_test Test passed')

    add_transaction_test()
    # wrong_type_transaction_check()
    validate_transaction_check()
    str_method_test()
    repr_method_test()
    balance_test()
    len_method_test()
    # wrong_validate_transaction_check()
    iter_test()
    getitem_method_test()
    reversed_method_test()
    comparison_tests()
    account_addition_test()
    account_addition_transactions_test()


if __name__ == '__main__':
    main()
