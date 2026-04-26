"""TUPLES
(1) What is tuples ? Tuples vs list
(2) Unpacking arguments
(3) ZIP
"""

print("====== What is tuples ? Tuples vs list ======")

# Java/PHP/NodeJS array => Python list

# literal
nums = [3, 4, 1, 2]
car_dic = {"brand": "Ferrari", "year": 1995}  # dictionary class

# constructor
letters = list("Hello world")
car_obj = dict(brand="Ferrari", year=1995)

fruits = ["olma", "lemon", "kiwi", "banan"]
print(f"before fruits => {fruits}")

fruits[2] = "melon"
print(f"after fruits => {fruits}")


print("====== Tuples ======")


animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("Umar", 100, True, None)
print(animals[0])
print(animals)
print(tuple_obj)

# try avoid these
people = "Norman", "Daniel"
animals = ("dog",)  # agar tupleni ustidan yozilsa hammasini o'rniga yozadi


print("====== Unpacking arguments ======")

nick = ["Ali", "Umar", "Huzuriy", "Abu"]
(x, y, z, a) = nick
(d, b, *c) = nick
print(f"the x {x} the y {y}")
print(c)  # list


# *args > tuple
def calculate(*args):  # *args => cheksiz positional argument
    total = 1
    for x in args:
        total *= x
    return total


result = calculate(12, 23, 21, 3, 4, 2, 4, 6)
result1 = calculate(4, 2, 4, 6)
result2 = calculate(4, 6)
print(result)
print(result1)
print(result2)


def person(**kwargs):  # **kwargs => nomlangan argumentlar
    return kwargs


result4 = person(name="Umar", year=2006, hobby="football")
print(result4)


def mixed(*args, **kwargs):
    return (args, kwargs)


result5, result6 = mixed(2, 4, True, "Ali", name="Ali", single=True)
print(result5)  # tuple
print(result6)  # dict
print(type(result5))
print(type(result6))


print("====== ZIP ========")  # index bilan tartiblaydi

tuple1 = (1, 2, 3, 4, 3, 1)
tuple2 = ("a", "b", "c")

zipped = zip(tuple1, tuple2)
print(zipped)  # list qilmaguncha manzil ko'rsatiladi 0x0000017CCA21EBC0>
result10 = list(zipped)
print(result10)
print(type(result10))

new_set = set(tuple1)
print(new_set)
