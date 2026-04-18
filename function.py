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
