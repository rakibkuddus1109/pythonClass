# Public attributes or method : Those attributes/methods which can be accessed anywhere without restriction

# class Student:
#     name = 'Rakib'  # Public attribute
#     email = 'rk@gmail.com'

#     def std_details(self):  # Public method
#         return "{} has email id {}".format(self.name, self.email)

# obj = Student()

# print(obj.name)
# print(obj.email)
# print(obj.std_details())


# Private attributes or method : attributes or methods which are not accessible outside of method
    # starts with '__'

class Student:
    name = 'Rakib'  # Public attribute
    __email = 'rk@gmail.com'

    def std_details(self):  # Public method
        return "{} has email id {}".format(self.name, self.__email)

    def __data(self):
        return "{} is valid".format(self.__email)

    def data(self):
        print(self.__data())

obj = Student()
# print(obj.data())

# <object-name>._<class-name>__<attribute-name> : to access private attribute

print(obj._Student__email)