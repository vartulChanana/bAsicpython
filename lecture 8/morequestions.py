#wap to create acc with 2 attribute (acc no and money)
#create methods for credit , debit and printing the balance
class Bank:
    def __init__(self,ac,money):
        self.ac=ac
        self.money=money

    def credit(self,amount):
        self.money += amount
        print("money credited to ur acc", amount)

    def debit(self,amount):
        if self.money >=amount:
            self.money-= amount
            print("money deducted",amount)
        else:
            print("LOW BALANCE,Money not deducted")
    
    def print_balance(self):
        print("YOUR BALANCE IS", self.money)

person1= Bank(12232323,232)
print(person1.ac,person1.money)
person1.credit(2333)
person1.debit(50100000)
person1.print_balance()