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
list = list("HEllo World")
print(f"{list} and its size {len(list)}")

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
