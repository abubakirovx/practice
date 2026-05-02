# def getMaxIndex(arr):
#     max = float("-inf")
#     indexMax = 0
#     for num in arr:
#         if num > max:
#             max = num
#             indexMax = arr.index(max)
#     return indexMax


# result = getMaxIndex([12, 333, 32, 7, 5, 45, 2, 6])
# print(result)


# '''E-TASK

# Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
# MASALAN: getReverse("hello") return qilsin "olleh" '''


# def getReverse(string):
#     arr = []
#     for i in string:
#         arr += i

#     arr.reverse()
#     arr= "".join(arr)
#     return arr


# result = getReverse(input("Enter word you want to reverse=>"))
# print(result)

"""
def richBankAtm():
    balance = 0
    print("Welcome to RBA (Rich Bank ATM) 🏦")
    sighn = input("Prees 0 to sigh up 🛠️ : ")
    if int(sighn) == 0:
        name = input("Please enter your fullname : ")
        name = name.title()
        phone = input(
            "Please enter your phone number with country code (ex:+82.00.0000.0000) ! 📞 : "
        )
        email = input("Please enter your Email without @gamil.com ! 📩 : ")
        email += "@gmail.com"
        password = input("Please enter your password (more than 4 number)🔐 : ")
        if len(password) > 3:
            # if name==True and phone == True and email ==True and password==True:
            print(f"Hi😊! Nice to see you {name} in our RBA branch ")
            print(
                "Choose service\n1.Balance\n2.Withdraw\n3.Deposit\n4.Info\n5.Change password\n6.Exit"
            )
            option = input("Enter : ")
            if int(option) == 1:
                print(f"Your balance {balance} usd💰")
            elif int(option) == 2:
                amount = int(input("Enter amount of withdraw : "))
                if balance < amount:
                    balance -= amount
                    print(
                        f"You withdrowed {amount} usd💰 !.Your current balance {balance} usd💰"
                    )
                else:
                    print(
                        f"Your balance is not enough !.Your current balance {balance} usd💰"
                    )
            elif int(option) == 3:
                money = int(input("Enter amount of deposit ! : "))
                balance += money
                print(
                    f"you deposited {money} usd💰 ! .Your current balance {balance} usd💰"
                )
            elif int(option) == 4:
                print(f"Name : {name}\nEmail : {email}\nPhone : {phone}")
            elif int(option) == 5:
                current_pass = int(input("Current password 🔑 : "))
                if current_pass == int(password):
                    new_pass = input("Enter new password (more than 4 number) 🔓 : ")
                    if len(new_pass) > 3:
                        password = new_pass
                    else:
                        print("Password must be more than 4 number ⚠️ try again !")
                else:
                    print("Current password is not same ❌ try again ! ")
            else:
                print(f"Thank for choosing RBA (Rich Bank ATM) 🏦 {name}")

        else:
            print("Password must be more than 4 number ⚠️ try again ! ")

    else:
        print("Wrong number ❌ try again ! ")


# richBankAtm()
"""

# def get_max_index(arr):
#     if not arr:
#         return -1
#     max_num = float("-inf")
#     max_index = 0
#     for index, value in enumerate(arr):
#         if value > max_num:
#             max_num = value
#             max_index = index
#     return max_index


# max_index = get_max_index([9, 2, 3, 2, 4, 7, 1, 3])
# print(max_index)


""" H-TASK (NodeJS)

shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
MASALAN: getPositive([1, -4, 2]) return qiladi "12" 
"""


def get_positive(arr):
    positive = [str(x) for x in arr if x > 0]
    result = "".join(positive)
    return result


positive_arr = get_positive([1, 2, 3, -4, 5, -7, 8])
print(type(positive_arr),'=>',positive_arr)


