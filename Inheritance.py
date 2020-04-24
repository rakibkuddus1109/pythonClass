# Inheritance : A class can get the properties from other class

# child class or sub class and parent class or super class

# class Employer:   # Parent/Super class
#     emp_address = "HitechCity"

# class Employee(Employer):   # Child/Sub class
#     emp_name = "Rakib"
#     # emp_address = "Hyderabad"

# obj = Employee()

# print(obj.emp_name)
# print(obj.emp_address)

# 5 types of inheritance:
    # Single inheritance
    # Multiple inheritance
    # Multilevel inheritance
    # Hybrid inheritance
    # Hierarchical inheritance

# Single inheritance: A class gets property from other single class

# class First:
#     course = "Python"

#     def course_details(self):
#         return "{} is trending now.".format(self.course)

# class Second(First):
#     course = "Django"

#     # def course_details(self):
#     #     return "{} is used for web development.".format(self.course)    

# obj = Second()

# # print(obj.course)
# print(obj.course_details())


# Multiple inheritance: Child class gets property from multiple parent classes

# class First:
#     course = "Python"

#     # def course_details(self):
#     #     return "{} is trending now.".format(self.course)

# class Second:
#     course = "Django"

#     def course_details(self):
#         return "{} is used for web development.".format(self.course)    

# class Third(First,Second):   # The flow will go by order how super class is inherited here
#     course = "Devops"

#     # def course_details(self):
#     #     return "{} is used for build/deployment.".format(self.course)   

# obj = Third()

# print(obj.course)
# print(obj.course_details())


# Multilevel inheritance: Child class gets property from parent class which again gets property from another parent one

# class First:
#     course = "Python"

#     def course_details(self):
#         return "{} is trending now.".format(self.course)

# class Second(First):
#     course = "Django"

#     # def course_details(self):
#     #     return "{} is used for web development.".format(self.course)    

# class Third(Second):   # The flow will go by order how super class is inherited here
#     course = "Devops"

#     # def course_details(self):
#     #     return "{} is used for build/deployment.".format(self.course)   

# obj = Third()

# print(obj.course)
# print(obj.course_details())

# Hybrid inheritance: Combination of multiple & multilevel inheritance

# class First:
#     # course = "Python"

#     def course_details(self):
#         return "{} is trending now.".format(self.course)

# class Second(First):
#     # course = "Django"

#     def course_details(self):
#         return "{} is used for web development.".format(self.course)    

# class Third:   # The flow will go by order how super class is inherited here
#     pass
#     course = "Devops"

#     def course_details(self):
#         return "{} is used for build/deployment.".format(self.course)   

# class Fourth(Second,Third):  # here order would be second (--> First) --> Third
#     pass
#     # course = "Machine Learning"

#     def course_details(self):
#         return "{} is hot topic now.".format(self.course)  

# obj = Fourth()

# print(obj.course)
# print(obj.course_details())


# Hierarchical inheritance: Multiple child classes are getting properties from single parent class

# class First:
#     course = "Python"

#     def course_details(self):
#         return "{} is trending now.".format(self.course)

# class Second(First):
#     # course = "Django"

#     def course_details(self):
#         return "{} is used for web development.".format(self.course)    

# class Third(First):   # The flow will go by order how super class is inherited here
#     pass
#     # course = "Devops"

#     # def course_details(self):
#     #     return "{} is used for build/deployment.".format(self.course)   

# obj = Third()

# print(obj.course)
# print(obj.course_details())

# obj1 = Second()

# print(obj1.course)
# print(obj1.course_details())


# Accessing the attribute from parent class:

class First:
    course = "Python"

    def course_details(self):
        return "{} is trending now.".format(self.course)

class Second:
    course = "Django"

    def course_details(self):
        return "{} is used for web development.".format(self.course)    

class Third(Second,First):   # The flow will go by order how super class is inherited here
    pass
    course = "Devops"

    def course_details(self):
        return "{} is used for build/deployment.".format(Second.course)   # Use class name here directly

obj = Third()

print(obj.course)
print(obj.course_details())
