''' CLASS
    (1) What is class ?
    (2) Ordinary vs static properties
    (3) Special/magic methods
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

print("==== Special methods =====")

# Python's most common special methods are below!
# __init__ , __new__ , __str__ , __call__ __getitem__ , __eq__ , __len__ ...


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, car_name, year):
        self.name = car_name
        self.year = year

    # method
    def start_engine(self):
        print(f"{self.name} is ready to drive -_-")

    def stop_engine(self):
        print(f"{self.name} stopped engine")

    def __str__(self):
        return f"{self.name} was produced {self.year}"

    def __call__(self):
        print("you call the method like a function")


my_car = Car("Ferrari", 2025) 
my_car.start_engine() #method 
my_car.stop_engine() #method 😎
about_car=Car.description #static
print(about_car) #static
my_car() #__call__
print(my_car) #__str__
your_car = Car("Cadilac", 2026)
your_car.start_engine()
