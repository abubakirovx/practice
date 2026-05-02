"""Array & Set
(1) Array
(2) Set
(3) Specific operators with set
"""

from array import array

# i = int, f = float
numbers = array("i", [1, 2, 3, 4, 5, 6])
print(numbers)

numbers.append(100)
numbers.insert(0, 14)
print(numbers)

numbers.remove(5)
numbers.pop()
print(numbers)

del numbers[0:2]
print(numbers)

print("==== Set =====")
# set of unique collection without keeping order!
# set delete duplicate value
new_numbers = array("i", [4, 2, 3, 4, 5, 6, 3, 8, 1])
new_set = set(new_numbers)

print("new_numbers=>", new_numbers)
print("new_set =>", new_set)

new_set.add(200)
print(new_set)

new_set.add(200)  # 2 marta qo'shilsa ham array duplicateni delete qiladi
print(new_set)

print("==== Specific operators with set =====")
#  |  &  -  ^

a = {1, 2, 3, 4}
b = {2, 3,5}

result1 = a | b  # union
print(f"result1=> {result1}") # a va b ning ikkalasida umumiy borlar
result2 = a & b  # intersection
print(f"result2=> {result2}") # a va b ning ikkalasidaham borlar
result3 = a - b  # difference
print(f"result3=> {result3}") # b dan a dagi bor sonlarni ayridi
result4 = b - a  # difference
print(f"result4=> {result4}") # a dan b dagi bor sonlarni ayridi 
result5 = a ^ b  # symmetric difference
print(f"result5=> {result5}") # a va b ning ikkalasidaham yo'qlar
