from datetime import date

from dateutil.rrule import rrule, MONTHLY


class Transaction(object):
    def __init__(self, amount, when):
        self.amount = amount
        self.when = when


class MonthlyTransaction(object):
    def __init__(self, amount, atday, times, start):
        self.amount = amount
        self.atday = atday
        self.times = times
        self.start = start

    def get_amount(self, atdate):
        rr = rrule(
            MONTHLY, dtstart=self.start, until=atdate, count=self.times,
            bymonthday=self.atday)
        return self.amount * rr.count()


class Wallet(object):
    def __init__(self, start=None):
        if start is None:
            start = date.today()
        self.start = start
        self.monthly = []
        self.transactions = []

    def transaction_monthly(
            self, description, amount, atday=1, times=None, start=None):
        if start is None:
            start = date.today()
        self.monthly.append(
            MonthlyTransaction(amount, atday, times, start))

    def transaction(self, description, amount, when=None):
        if when is None:
            when = date.today()
        self.transactions.append(Transaction(amount, when))

    def get_amount(self, atdate=None):
        if atdate is None:
            atdate = date.today()
        amount = sum([t.amount for t in self.transactions if t.when <= atdate])
        for i in self.monthly:
            amount += i.get_amount(atdate)
        return amount
