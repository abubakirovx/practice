''' Comprehension
    (1) What is comprehension ? & list comp
    (2) set and dictionary comp.
'''
print("=======What is comprehension ? & list comp=========")
# Comprehension acts like spread operator!

'''Comprehension general syntax:
   a) *iterable
   b) <expression> for item in itarable
   c) <expression> for item in itarable <condition>
'''
# list comp

numbers = [1, 2, 3, 4, 1, 20]
a = numbers
list_number = [*numbers]  # a version
print(f"list_number {list_number}")
print(numbers is list_number)
print(numbers is a)
print(id(numbers), id(a), id(list_number))

people = [('Umar', 20), ('Ali', 18), ('Huzuriy', 22)]
list_people = [person[0] for person in people]  # b version
print(list_people)

print("--------")
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33),
]

list_cars = [car[0] for car in cars if car[1] > 80]  # b version
print("Cars which  are older than 80 years =>", list_cars)
