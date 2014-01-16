from datetime import date
import unittest

from mywallet.core import Wallet


class MainTest(unittest.TestCase):
    def setUp(self):
        self.w = Wallet(start=date(2014, 1, 1))

    def test_transaction(self):
        w = self.w
        w.transaction("freela", 50)
        w.transaction("lotofacil bar do ze", 15)
        w.transaction("conta bar do ze", -20)
        self.assertEqual(w.get_amount(), 45)

    def test_transaction_monthly(self):
        w = self.w
        w.transaction_monthly("salary", 1000, atday=5, start=w.start)
        w.transaction_monthly("freela", 50, atday=1, times=2, start=w.start)
        w.transaction_monthly("internet", -100, atday=7, start=w.start)
        self.assertEqual(w.get_amount(date(2014, 3, 5)), 2900)


if __name__ == "__main__":
    unittest.main()