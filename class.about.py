''' CLASS
    (1) What is class ?
    (2) Ordinary vs static properties
    (3) Special methods
'''

print("==== What is class =====")
# class - blueprint for object creation!
# structure > state, constructor, method


class Person():
    # state
    message = "static state property"

    # constructur
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"Hi ,my name {self.name} and i am {self.age} years old !")

    @classmethod
    def explain(cls):
        print('this is static method of Python ! ')


person1 = Person("Umar", 20)
person2 = Person("Ali", 22)
person3 = Person("Norman", 24)


print("==== Ordinary vs static properties =====")

# ordinary state
name = person1.name
print("person1 ning ismi=>", name)

age = person2.age
print('person2 ning yoshi=>', age)

# ordinary method
person1.introduce()
person2.introduce()
person3.introduce()
person1.say_age()
person2.say_age()
person3.say_age()

# static property
new_message = Person.message
print(f"static message=> {new_message}")

Person.explain()