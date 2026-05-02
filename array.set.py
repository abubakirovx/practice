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
