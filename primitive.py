print("==== number =====")
# in JAVA , variable is a name storage location!
# in Python, variable is named reference!

count = 100
print(f"count : {count}")
count_type = type(count)
print(f"the count : {count} and type : {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("==== string =====")
# METHODS: upper() lower() title() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"the type of course : {result}")

result = course.title()  # only first letter of word is in UPPERCASE
print(f"the result (1) : {result}")

result = course.upper()
print(f"the result (2) : {result}")

# change first argument to second =>"MasterClass"
result = course.replace("FullStack", "MasterClass")
print(f"the result (3) : {result}")

print(f"original version : {course}")

print("==== boolean =====")
# functions > type() input() bool() int() str()
y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"this input 'y' is numeric ? {result}")

# TRUTHY (many) => True, 100, " ", -100, "UMAR", ...
# FALSY (4)     => False, "", 0, None

test_falsy = ""
print(f"THE FALSY (1) : {bool(test_falsy)}")

test_falsy = "" or False or None or 0
print(f"THE FALSY (2) : {bool(test_falsy)}")

# thsi is not FALSY becouse of "Ali" is TRUTHY
test_falsy = "" or False or None or 0 or "Ali"
print(f"THE FALSY (3) : {bool(test_falsy)}")
