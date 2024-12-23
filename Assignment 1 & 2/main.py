class account:
    def open_account(self):
        self.acc_no = 1
        self.balaance = 0
    def balance_enquiry(self):
        print(self.acc_no)
        print(self.balance)
    def open_account(self):
        self.acc_no = 1
        self.balance = 0
    def deposit(self,amt):
        self.balance += amt
    def withdraw(self,amt):
        self.balance -= amt
        print(self.balance)
ac = account()
ac.open_account()
ac.balance_enquiry()
ac.deposit(amt)
ac.balance_enquiry()
print(ac.acc_no)