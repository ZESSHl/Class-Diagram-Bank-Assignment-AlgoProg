class Account:
    def __init__(self, balance=500_000):
        if balance > 500_000:
            self.balance = balance
        else:
            self.balance = 500_000

    def getBalance(self):
        return self.balance

    def deposit(self, set):
        if set > 0:
            self.balance = self.balance + set
            return True
        return False
    
    def withdraw(self, set):
        if set < self.balance:
            self.balance = self.balance - set
            return True
        return False
    

acc1 = Account(500_001)

print(acc1.getBalance())
amt = 600000

if acc1.deposit(amt): 
    print(acc1.getBalance())
else:
    print("Invalid Amount")

amt = 600000
if acc1.withdraw(amt):
    print(acc1.getBalance())
else:
    print("Invalid Amount")

class Customer:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.account = None

    def getFirstName(self):
        return self.first
    
    def getLastName(self):
        return self.last
    
    def getAccount(self):
        return self.account
    
    def setAccount(self, acct):
        self.account = acct

class Bank:
    def __init__(self, bankname):
        self.bankname = bankname
        self.customers = []         
        self.numberOfCustomers = 0 

    def addCustomer(self, first, last):
        new_customer = Customer(first, last)
        self.customers.append(new_customer)
        self.numberOfCustomers += 1
        return new_customer  

    def getNumOfCustomers(self):
        return self.numberOfCustomers

    def getCustomer(self, index):
        if 0 <= index < self.numberOfCustomers:
            return self.customers[index]
        return None
        
acc1 = Account(500_001)
print("Account start:", acc1.getBalance())       
if acc1.deposit(600_000):
    print("After deposit:", acc1.getBalance())      
if acc1.withdraw(600_000):
    print("After withdraw:", acc1.getBalance())     


bank = Bank("Mandiri")
c1 = bank.addCustomer("Jeff", "Koo")

print("Bank:", bank.bankname)
print("Total customers:", bank.getNumOfCustomers()) 


c1_acct = Account(700_000)
c1.setAccount(c1_acct)
c1.getAccount().deposit(200_000)
print("First customer:", c1.getFirstName(), c1.getLastName())
print("Balance:", c1.getAccount().getBalance())      

print("Invalid index returns:", bank.getCustomer(5)) 