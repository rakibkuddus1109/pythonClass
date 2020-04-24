# oops : object oriented programming

# class : details explaination of an object (blueprint of object)
# object : instance/variable of a class (ex: your house)
    # instance means calling the class

# Syntax to declare class

"""
class <class name>:
    <statements>
"""

# Class name : it is recommended to start with upper case letter

# class Student:
#     name = "Rakib"
#     email = "rk@gmail.com"

#     print("{} has email id: {}".format(name,email))

# def Student():
#     name = "Rakib"
#     email = "rk@gmail.com"

#     print("{} has email id: {}".format(name,email))

# Without calling function it won't print anything in abov example but class does print. We don't have to call the class.

# Object creation: Caling the class

# class Student:
#     name = "Rakib"
#     email = "rk@gmail.com"

#     print("{} has email id: {}".format(name,email))

# obj = Student() # Instance of the class : Object
# print(obj)
# print(obj.name)
# print(obj.email)

# print(Student.name)
# print(Student.email)

# Attribute : Variable that is defined inside class
    # Class attribute
    # Instance attribute

# class Student:
#     name = "Rakib"
#     email = "rk@gmail.com"

#     def std_details(self):  # self : default value that python considers for function inside class
#         print("{} has email id: {}".format(self.name,self.email))

# obj = Student()
# print(obj)
# def syntax defined inside class is called as method
    # class method
    # instance method (with self)

# Constructor : Passing value at the class call

# __init__ : constructor, no need to call this method (auto called when class is called)

class Student:

    def __init__(self,name,email):  # self : default value that python considers for function inside class
        self.name = name  # making it accessible anywhere in class
        self.email = email
        # print(name)
        # print(email)

obj = Student("Rakib","rk@gmail.com")

print(obj.name)
print(obj.email)