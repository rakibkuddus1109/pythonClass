# Attributes : Variables or arguments declared inside the class
    # Class Attributes : declared outside of all methods but inside the class, can be accessed with class name
    # Instance/Object Attributes : declared as arguments of methods inside class which can be accessed with object

# Class/Instance Attributes

# class Employee:
#     emp_name = "Rakib"
#     emp_com = "Wells"

#     def __init__(self,emp_name,emp_com):
#         self.emp_name = emp_name
#         self.emp_com = emp_com
#         pass

# obj = Employee("Rafaat","Aala")

# print(Employee.emp_name)  # Class attributes
# print(Employee.emp_com)

# print(obj.emp_name)  # Instance attributes
# print(obj.emp_com)


# Mehtods : Functions declared inside the class
    # Class Methods : method with 'cls' as default argument with @classmethod decorator, can be access with both class & object
    # Instance Methods : method with 'self' as default argument, can be accessed with object

class Employee:

    def __init__(self,emp_name,emp_com):
        self.emp_name = emp_name
        self.emp_com = emp_com
        pass

    def emp_details(self):    # instance method
        return "{} works for {} company".format(self.emp_name,self.emp_com)

    @classmethod  # decorator in python
    def cls_emp_details(cls,emp_name,emp_com):   # class method
        cls.emp_name = emp_name
        cls.emp_com = emp_com
        return "{} has employee named {}".format(emp_com,emp_name)

    @classmethod
    def cls_emp_salary(cls,salary):
        return "{} gets salary amount {}".format(cls.emp_name,salary)

    @staticmethod
    def static_details(emp_state,emp_city):
        return "{} city is in {} state".format(emp_city,emp_state)

obj = Employee("Rakib","Wells")
print(obj.emp_details())

# print(Employee.cls_emp_details("Rafaat","Aala"))
print(obj.cls_emp_details("Rafaat","Aala"))

print(obj.emp_name)     # comes from instance method -- Rakib
print(Employee.emp_name)     # comes from class method -- Rafaat

print(obj.cls_emp_salary("5L"))

print(obj.static_details("Telangana","Hyderabad"))