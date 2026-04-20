''' CLASS deep diving
    (1) ENCAPSULATION
    (1) INHERITENCE
    (1) POLIMORPHISM
'''

print("====== INHERITANCE ======")
# PARENT > CHILD
# parent only provides only public and protected properties(state+method) to children


class Animal():  # Parent   class Animal: => True   class Animal(object): => True
    description = "the class parent of animals"

    def __init__(self, voice):
        self._status = "animal is alive"
        self._voice = voice

    def make_voice(self):
        print(f"the animal can make voice =>{self._voice}")


class Dog(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.__name = name
        self.__sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"the {self.__name} says {self.__sound} {self.__sound}!")

    def protect(self):
        print(f"Yes , you are under my defence ☠️")


class Cat(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.__name = name
        self.__sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"the {self.__name} says {self.__sound} {self.__sound}!")

    def play(self):
        print(f"Yes,i am playing ")


class Fish(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.__name = name
        self.__sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"the {self.__name} says {self.__sound} {self.__sound}!")

    def swim(self):
        print(f"Yes ,i can swim")


my_dog = Dog("REX", "wow", True)

my_dog.introduce()
my_dog.protect()
print(my_dog.description)
print("dog.status=>", my_dog._status)
my_dog.make_voice()

my_cat = Cat("Garfild", "myeow", True)

my_cat.introduce()
my_cat.play()
print(my_cat.description)
print("cat.status=>", my_cat._status)
my_cat.make_voice()

my_fish = Fish("Nemo", "bliq bliq", False)

my_fish.introduce()
my_fish.swim()
print(my_fish.description)
my_fish.make_voice()

print("+++++++++++")
my_animals = Animal(True)

my_animals.make_voice()
print(my_animals.description)

# my_fish > Fish > Animal > object
print(isinstance(my_fish, Fish))
print(isinstance(my_fish, Animal))
print(isinstance(my_fish, object))

# Fish > animal > object
print(issubclass(Fish, Animal))
print(issubclass(Animal, object))
print(issubclass(Fish, object))
