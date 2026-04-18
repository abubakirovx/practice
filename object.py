''' OBJECTS
  (1) What is object ?
  (2) Iterable objects & RANGE
  (3) DICTIONARY
  (4) Error handling system

'''
import array  # package/module
import math  # package
from math import ceil  #
print("============ What is object ? ============")
# An object has state and method properties
# Everything is object in Pyhton

print(type('Hello World'))
print(type(100))
print(type(True))
print(type(math))
print(type(array))


# Paradigm > Functional programming & OOP = Object-oriebted Programming
# OOP 4 concepts > ABSTRACTION | ENCAPSULATION | INHERITANCE | POLIMARPHISM
result = math.ceil(34.2)  # CALL
result2 = ceil(34.9)  # ceil tepada import bo'lgan
print(result)
print(result2)


print("============ Error handling system ============")

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print('passed here')
    result3 = car_dict["made_in"]
    print(result3)
except KeyError as err:
    print('No made_in state property found',err)

