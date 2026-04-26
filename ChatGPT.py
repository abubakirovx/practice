# a = True
# b = 10

# print(int(True))
# print(int(False))

# b = 100  # 4


# def fun(a):  # 3 defult
#     # b = 700   #1
#     c = a*b
#     return c


# result = fun(30)  # 2
# print(f"result => {result}")

# def i_cloud(name, age):
#     if age >= 18:
#         print(f"salom {name} you can enter")
#     else:
#         print(f"sorry {name} can't enter at this {age} age")


# i_cloud("Norman", 15)

# code1 = 1234
# code2 = 4321
# floor1 = 1
# floor2 = 2
# home1 = 101
# home2 = 102


# def home_check(name, home, pin, floor):
#     if home != home1 or pin != code1 or floor != floor1 or home != home2 or pin != code2 or floor != floor2:
#         print(f"{name} you dont live here !")
#     elif home == home1:
#         print(f"Hi {name} welcome to home {home1}")
#     else:
#         print(f"Hi {name} welcome to home {home2}")


# home_check()

# agar son musbat bo‘lsa → "positive"
# agar manfiy bo‘lsa → "negative"
# agar 0 bo‘lsa → "zero"

# a = -1
# if a == 0:
#     print("zero")
# elif a > 0:
#     print("positive")
# else:
#     print("negative")

# Car nomli class yoz:
# brand
# year
# info() method bo‘lsin (print qilsin)

# class Car():
#     def __init__(self,brand,year):
#         self.__brand=brand
#         self.__year=year

#     def info(self):
#         print(f"the {self.__brand} was produced {self.__year}")


"""
1.bunda javob float chiqadi chunki kasrli sonlar float claasiga butun son int classiga tegishli
2.bilmiman o'rgat
3.pythondagilarni bilmiman o'rgat
4.bilmadm buni ham
5.True qaytaradi chunki string ham truthy ga kiradi
6.8 chunki default b=5
7.buni o'rgatmadi hali unchalik kerak emas deb
8.bilmadm
9.class bu object yasovchi shablonn yani qolib
10.__init__ ni men class yasashda constractor uchun ishlatyabman
11.self bu jsdagi this bilan birxil yani object ichidan qidiradi
12.bilmadm
13.@classmethodni bilaman bu static method yasashda ishlatiladi
14.bu parent va child tushunchasi yani child o'zining ichida yo'q method yoki statelarni otadan olaveradi
15.bilmadm
16.otada ham boladaham bir xil nom bilan method borligi
17. bular jsdagi && || ! kabi ishlaydi
18.False va True chunki 0 Falsy
19.for takrorlanish soni aniq bo'lganda ishlatiladi while esa kopincha aniqmasligida
20.break o'sha zahoti yakunlaydi continue esa  tashlab o'tib ketadi
21.0,2
22.tuple (1,2,3) shunaqa korinishda yozilishini bilaman va o'zgartirib bolmasligini ham lekn listni o'tmadik hali
"""


# arr = [10, 20, 30, 40, 12]

# arr.pop()

# print(arr)  # [10, 20]


def richBankAtm():
    balance = 0
    print("Welcome to RBA (Rich Bank ATM) 🏦")

    sighn = input("Press 0 to sign up 🛠️ : ")
    if sighn != "0":
        print("Wrong number ❌ try again !")
        return

    name = input("Please enter your fullname : ").title()
    phone = input("Enter phone (+code) 📞 : ")
    email = input("Enter email (without @gmail.com) 📩 : ") + "@gmail.com"
    password = input("Enter password (min 4 chars) 🔐 : ")

    if len(password) < 4:
        print("Password too short ❌")
        return

    print(f"Hi 😊 {name}!")

    # 🔁 LOOP boshlanadi
    while True:
        print("\nChoose service:")
        print("1. Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Info")
        print("5. Change password")
        print("6. Exit")

        option = input("Enter: ")

        if option == "1":
            print(f"Your balance: {balance} USD 💰")

        elif option == "2":
            amount = int(input("Enter withdraw amount: "))
            if amount > balance:
                print("Not enough balance ❌")
            else:
                balance -= amount
                print(f"Withdrawn: {amount} USD 💰")

        elif option == "3":
            money = int(input("Enter deposit amount: "))
            balance += money
            print(f"Deposited: {money} USD 💰")

        elif option == "4":
            print(f"Name: {name}\nEmail: {email}\nPhone: {phone}")

        elif option == "5":
            current = input("Current password 🔑: ")
            if current == password:
                new_pass = input("New password 🔓: ")
                if len(new_pass) >= 4:
                    password = new_pass
                    print("Password changed ✅")
                else:
                    print("Too short ❌")
            else:
                print("Wrong password ❌")

        elif option == "6":
            print(f"Goodbye {name} 👋")
            break  # 🔥 loopni to‘xtatadi

        else:
            print("Invalid option ❌")


richBankAtm()

nums = [10, 15, 20, 25, 30]
find = map(lambda x: x * 2, filter(lambda x: x > 20, nums))
print(list(find))

nums = [5, 10, 15, 20, 25, 30]
get = map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums))
print(list(get))

"""nums = [12, 5, 8, 15, 22, 3, 18]

👉 Shuni list comprehension bilan qil:

🎯 Shartlar:
faqat juft sonlarni ol
faqat 10 dan katta bo‘lsin
har birini kvadratga oshir (x²)
natijani listda qaytar
🔥 Kutilayotgan natija
[144, 484, 324]
"""
nums = [12, 5, 8, 15, 22, 3, 18]

result = [x * x for x in nums if x % 2 == 0 and x > 10]
print(result)
