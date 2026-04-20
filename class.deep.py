''' CLASS deep diving
    (1) ENCAPSULATION
    (1) INHERITENCE
    (1) POLIMORPHISM
'''

print("===== Encapsulation=====")
# ENCAPSULATION > public, __private, _protected


class Account():
    # state
    description = "This class makes bank account"\

    # constuctor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"Mr(s) {self.__owner}! Your balance {self.__amount} usd")

    def deposit(self, money):
        self.__amount += money
        print(f"{money}$ added into your balance")

    def withdraw(self, money):
        self.__amount -= money
        print(f"{money}$ withdrow from your balance !")

    @property
    def holder(self):      # can use like a state not like a function
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print(f"{self.__owner} ! your name changed to {new_owner} via holder.setter")
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print(f"{self.__owner} ! your name changed to {new_owner}")
        self.__owner = new_owner


my_account = Account("Umar", 0)
my_account.deposit(200)
my_account.get_balance()
my_account.deposit(1000)
my_account.get_balance()
my_account.withdraw(300)
# print(my_account.__owner) #ERROR
# my_account.__amount = 10000000  # not changed
# my_account.__owner = "Ali"  # not changed
# my_account.get_balance()

try:
    result = my_account.__amount
    print("result=>", result)
except Exception as err:
    print("No target state found", err)

print(my_account.holder)  # state> now have permission  for READ-ONLY owner !
my_account.change_ownership("Huzuriy")  # now have permission for CHANGE owner !
my_account.holder = "Abu"
my_account.get_balance()
