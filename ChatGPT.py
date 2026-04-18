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

code1 = 1234
code2 = 4321
floor1 = 1
floor2 = 2
home1 = 101
home2 = 102


def home_check(name, home, pin, floor):
    if home != home1 or pin != code1 or floor != floor1 or home != home2 or pin != code2 or floor != floor2:
        print(f"{name} you dont live here !")
    elif home == home1:
        print(f"Hi {name} welcome to home {home1}")
    else:
        print(f"Hi {name} welcome to home {home2}")


home_check()
