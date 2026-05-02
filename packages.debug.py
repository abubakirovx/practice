''' Packages & Debugging
    (1) Python Packages & Core Package 
    (2) Packages Manager & External Package
    (3) Debugging
'''
from PIL import Image
from turtle import Screen, Turtle, done
print("===== Python Packages & Core Package =====")
'''Python Packages /Modules: Core, File and External '''
# Core Packages > https://docs.python.org/3/library

# t=Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)

# done()

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()  # YOU MUST CLOSE

# with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)  # auto closed by with


print("===== Packages Manager & External Package =====")
'''Package Manager 
   Python > pip pipenv
   NodeJS > npm yarn
   PHP > Composer
   MacOS > brew
'''
# External Packages > https://pypi.org/

'''
with Image.open("material/img.jpg") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")
'''


print("===== Debugging =====")


def get_summary(*args):  # DEFINE
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # solve the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5)  # CALL
print("result", result)
