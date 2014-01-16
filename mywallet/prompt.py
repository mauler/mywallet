from decimal import Decimal
import cmd
import re


class Prompt(cmd.Cmd):

    def __init__(self, wallet=None, *args, **kwargs):
        self.wallet = wallet
        cmd.Cmd.__init__(self, *args, **kwargs)

    def p(self, line):
        self.stdout.write(line)
        self.stdout.write("\n")

    def do_transaction(self, line, description=None):
        parts = line.split(" ")
        amount = Decimal(parts[0])
        times = None
        match = re.match("(\d+)[x,X]", parts[1])
        if match:
            times = int(match.group(1))

        if 'monthly' in parts:
            self.wallet.transaction_monthly(description, amount, times=times)
        else:
            self.wallet.transaction(description, amount)

    def do_deposit(self, line):
        return self.do_transaction(line, "deposit")

    def do_withdraw(self, line):
        return self.do_transaction(line, "withdraw")

    def do_amount(self, line):
        print repr(line)
        print self.wallet.get_amount()

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    from core import Wallet
    p = Prompt(Wallet())
    p.onecmd("deposit monthly 1000 2x")
    p.onecmd("deposit 550")
    p.onecmd("deposit 550")
    p.onecmd("withdraw 500")
    p.onecmd("amount")
