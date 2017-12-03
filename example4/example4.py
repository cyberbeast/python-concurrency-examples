from threading import Thread
import time

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        newBalance = self.balance + amount
        print("Depositing: %d, new balance is %d" % (amount, newBalance))
        self.balance = newBalance
    
    def withdraw(self, amount):
        newBalance = self.balance - amount
        print("Withdrawing: %d, new balance is %d" % (amount, newBalance))
        self.balance = newBalance
    
    def getBalance(self):
        return self.balance

def triggerDeposits(bankAccount, amount, count):
    print("In here")
    for i in range(count):
        bankAccount.deposit(amount)
        # time.sleep(1)

def triggerWithdraws(bankAccount, amount, count):
    for i in range(count):
        bankAccount.withdraw(amount)
        # time.sleep(1)

if __name__ == '__main__':
    bAcct = BankAccount()
    amount = 100
    repetitions = 100
    threads = 100

    for i in range(threads):
        t1 = Thread(target=triggerDeposits, args=(bAcct, amount, repetitions,))
        t2 = Thread(target=triggerWithdraws, args=(bAcct, amount, repetitions,))
        t1.start()
        t2.start()
        
