"""OPERATORS & CONDITIONS
(1) Operators
(2) Condition
(3) Logical Operators
"""

print("===== Operators =====")
# + - > >= < <= * / is   // % += -= **

a = 19
b = 5

print(a / b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b**2", b**2)
print("b**3", b**3)

print("=" * 10)

c = dict(name="Umar", age=20)
d = dict(name="Umar", age=20)
e = c

print("c==d :", c == d)  # only value
print(id(c), id(d))
print(id(c), id(e)) # id is similar

data = c is d
data1 = c is e

print("c is d :", data)
print("c is e :", data1)
