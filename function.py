''' FUNCTIONS 
  (1) DEFINE vs CALL
  (2) Parametrs vs Argument
  (3) Keyword & default arguments
  (4) Scope

'''

print("(======DEFINE (parametr) vs CALL (argument)======)")
# build in function  > print() type()
# Function - reusable block of code!
# Instead of block {} in JAva, Python uses Indentation


# DEFINE - built (parametr)
def greet(a):
    print('salom', a)    # Void function


def greeting(b):
    print('salom', b)
    return b             # Return function


# CALL  - execute (argument)
greet("Umar")

result = greeting("Ali")
print(result)


print("(====== Keyword & default arguments ======)")

# DEFINE


def give_greet(name, age=22):
    print(f'give_greet function is executed')
    return f"Hi {name},you are {age} years old!"


# CALL

result2 = give_greet(name="Huzuriy", age=20)
print('result2=> ', result2)

result3 = give_greet('Umar')
print(result3)


print("(====== Scope ======)")

# DEFINE

b = 100


def calculate(a, b):
    c = a*b
    print(f"c value: {c}")


# CALL
calculate(3, 5)


# b = 100  # 4


# def cal(a):  # 3 defult
#     # b = 700   #1
#     c = a*b
#     return c


# result5 = cal(30)  # 2
# print(f"result5 => {result5}")
