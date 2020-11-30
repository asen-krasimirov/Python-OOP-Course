from solutions.account import Account
import unittest


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account_one = Account('Test One')
        self.account_two = Account('Test Two', 100)

    def test_init_creates_correct_attrs(self):
        owner_one, amount_one, transactions_one = self.account_one.owner, self.account_one.amount, list(self.account_one._transactions)
        owner_two, amount_two, transactions_two = self.account_two.owner, self.account_two.amount, list(self.account_two._transactions)

        self.assertEqual(owner_one, 'Test One')
        self.assertEqual(amount_one, 0)
        self.assertEqual(transactions_one, [])

        self.assertEqual(owner_two, 'Test Two')
        self.assertEqual(amount_two, 100)
        self.assertEqual(transactions_two, [])

    def test_add_transaction_method_adds_amount_to_transactions(self):
        self.account_one.add_transaction(100)
        self.assertEqual([100], self.account_one._transactions)

    def test_add_transactions_raises_value_error_when_non_integer_is_given(self):
        self.assertRaises(ValueError, self.account_one.add_transaction, 'test')

    def test_balance_property(self):
        self.account_one.add_transaction(100)
        self.account_one.add_transaction(250)
        result = self.account_one.balance
        self.assertEqual(350, result)

        self.account_two.add_transaction(100)
        self.account_two.add_transaction(250)
        result = self.account_two.balance
        self.assertEqual(450, result)

    def test_validate_transaction_happy_result(self):
        self.account_one.validate_transaction(self.account_one, 100)
        self.assertEqual([100], self.account_one._transactions)

        self.account_one.validate_transaction(self.account_two, -100)
        self.assertEqual([-100], self.account_two._transactions)

    def test_validate_transaction_return_value(self):
        result = self.account_one.validate_transaction(self.account_one, 100)
        self.assertEqual('New balance: 100', result)

    def test_validate_transactions_raises_value_error_when_balance_goes_below_zero(self):
        self.assertRaises(ValueError, self.account_one.validate_transaction, self.account_one, -100)
        self.assertRaises(ValueError, self.account_one.validate_transaction, self.account_two, -200)

    def test_magic_method_string(self):
        result = str(self.account_one)
        expected_result = 'Account of Test One with starting amount: 0'
        self.assertEqual(expected_result, result)

    def test_magic_method_repr(self):
        result = repr(self.account_one)
        expected_result = 'Account(Test One, 0)'
        self.assertEqual(expected_result, result)

    def test_magic_method_len(self):
        self.account_one.add_transaction(100)
        result = len(self.account_one)
        self.assertEqual(1, result)

    def test_iterating_through_all_transactions(self):
        self.account_one.add_transaction(100)
        self.account_one.add_transaction(200)
        self.account_one.add_transaction(300)

        def local_transaction_generator():
            for transaction in self.account_one:
                yield transaction

        transactions = local_transaction_generator()
        self.assertEqual(self.account_one._transactions, list(transactions))

    def test_getting_items_by_index(self):
        self.account_one.add_transaction(100)
        elem = self.account_one[0]
        self.assertEqual(100, elem)

    def test_magic_method_reversed(self):
        self.account_one.add_transaction(100)
        self.account_one.add_transaction(200)
        self.account_one.add_transaction(300)

        result = list(reversed(self.account_one))
        expected_result = [300, 200, 100]
        self.assertEqual(expected_result, result)

    def test_comparing_accounts(self):
        acc1, acc2 = self.account_one, self.account_two

        self.assertFalse(acc1 > acc2)
        self.assertFalse(acc1 >= acc2)
        self.assertFalse(acc1 == acc2)
        self.assertFalse(acc2 < acc1)
        self.assertFalse(acc2 <= acc1)
        self.assertFalse(acc1 != acc1)

        self.assertTrue(acc2 > acc1)
        self.assertTrue(acc2 >= acc1)
        self.assertTrue(acc2 >= acc2)
        self.assertTrue(acc2 == acc2)
        self.assertTrue(acc1 < acc2)
        self.assertTrue(acc1 <= acc2)
        self.assertTrue(acc1 <= acc1)
        self.assertTrue(acc1 != acc2)

    def test_adding_two_accounts_together(self):
        self.account_one.add_transaction(123)

        new_account = self.account_one + self.account_one
        new_owner, new_amount = new_account.owner, new_account.amount
        transactions = new_account._transactions
        expected_representation = 'Account of Test One&Test One with starting amount: 0'

        self.assertEqual('Test One&Test One', new_owner)
        self.assertEqual(0, new_amount)
        self.assertEqual([123, 123], transactions)
        self.assertEqual(expected_representation, str(new_account))

    # def test_is_validate_transactions_method_static(self):
    #     self.assertIs(type(self.account_one.validate_transaction), type(lambda: None))


if __name__ == '__main__':
    unittest.main()
