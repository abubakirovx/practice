"""List
(1) Working with lists
(2) List methods
(3) Lambda function
(4) enumerate,map and filter
"""

print("============ Working with lists ================")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Umar", "age": 20}  # dictionary
people = ("Ali", "Norman", "Huzuriy")  # tuple
groups = ["FanTalk", "MIT", "Instagram"]  # list
for team in groups:
    print(f"the team {team}")

# constuctor
new_list = list("HEllo World")
print(f"{new_list} and its size {len(new_list)}")

fruits = ["olma", "behi", "olcha", "gilos", "orik"]
a = fruits[0]
b = fruits[0:2]  # 0 va 1 index kiradi 2 kirmaydi
c = fruits[::2]  # 0 dan boshlab bitta tashlab ikkinchi qiymatni oladi
d = fruits[::-1]  # reverse qiladi -1 teskaridan
print("a=>", a)
print("b=>", b)
print("c=>", c)
print("d=>", d)

print("============ List methods ================")
# methods =>
# append(), insert(), pop(), remove(), clear(), sort()=> MUTABLE
# index(), sorted()=> INMUTABLE

letters = ["a", "b", "c"]
print(letters)

letters.append("d")  # add behind
print(letters)

e = letters.pop()  # remove behind
print(letters, "removed value=>", e)

letters.insert(0, "A")  # add front
print(letters)

e1 = letters.pop(0)  # remove front
print(letters, "removed value=>", e1)

print("============")

animals = ["dog", "cat", "fish", "lion", "cow"]
print(animals)

animals.remove("lion")
print(animals)

del animals[1:3]  # 1 chi index kiradi 3 kirmaydi
print(animals)

result = animals.index("cow")
print(f"the index of cow => {result}")

animals.clear()  # clear all value
print(animals)

# animals.append("cow")
# print(animals)

if "cow" in animals:
    print("index of cow => ", animals.index("cow"))
else:
    print("cow is not exist")

print("============")

numbers = [2, 23, 23, 12, 45, 34, 21, 5]
numbers.sort()  # sort default
print("sort default", numbers)

numbers = [2, 23, 23, 12, 45, 34, 21, 5]
numbers.sort(reverse=True)  # sort reverse
print("sort reverse", numbers)


# inmutable sorted(list)
numbers = [61, 23, 23, 34, 21, 5]

sonlar = sorted(numbers)
print(sonlar)
print(numbers)

print("============  Lambda ================")
# lambda is small anonymous function!


def calculate(a, b):
    return a + b


result = calculate(34, 65)
print(result)

people = [("Umar", 20), ("Ali", 22), ("Norman", 24), ("Huzuriy", 19), ("Buhoriy", 60)]

people.sort()  # sort by name
print("sort by name=>", people)

# sort by age via lambda
people.sort(
    key=lambda person: person[1]
)  # 1 index bu people ichida name emas ageni bildiradi
print("sort by age=>", people)

print("============ enumerate,map and filter ================")
# enumerate for index & value

animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("element", element)

for index, value in enumerate(animals):
    print(f"the index {index} the value is {value}")

# similar in dictionaries
car_obj = dict(brand="ferrari", year=2025)
result = car_obj.items()
# print(result)
for key, value in result:
    print(f"the key is {key} the value is {value}")




# map
print("========")

cars = [("Ferrari", 78), ("Toyota", 87), ("Audi", 116), ("BMW", 109), ("Pegani", 33)]

new_cars = []  # literal uslubda listdagi brandlarni olish
for car in cars:
    new_cars.append(car[0])
print(new_cars)

result1 = map(lambda car: car[0], cars)  # map orqali listdagi brandlarni olish
new_cars = list(result1)
print(new_cars)

# list comprehension 
result2 = [x[0] for x in cars]
print("list comprehension =>", result2)

# filter 
result3=filter(lambda x:x[1]>100,cars)
print("filter",list(result3))
