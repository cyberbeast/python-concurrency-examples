from threading import Thread
import threading
import time

class BankAccount:
    def __init__(self):
        self.lock = threading.Lock()
        self.sufficientBalanceCondition = threading.Condition(self.lock)
        self.balance = 0
    
    def deposit(self, amount):
        self.lock.acquire()
        try:
            newBalance = self.balance + amount
            self.balance = newBalance
            print("Depositing: %d, new balance is %d" % (amount, newBalance))
            self.sufficientBalanceCondition.notifyAll()
        finally:
            self.lock.release()
            
    
    def withdraw(self, amount):
        self.lock.acquire()
        try:
            while(self.balance < amount):
                self.sufficientBalanceCondition.wait()
            newBalance = self.balance - amount
            self.balance = newBalance
            print("Withdrawing: %d, new balance is %d" % (amount, newBalance))
        finally:
            self.lock.release()
    
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
        
