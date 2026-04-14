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


