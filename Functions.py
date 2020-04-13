# Functions : Set of statements to perform a specific task
    # Function reduces no. of line of codes i.e. code resusability is implemented

"""
# def -- keyword

def functionname():
    Statements/ines of code
"""

# a=34
# b=26
# def mathoperation():
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# # Functiona has to be called to execute the statements inside function

# mathoperation()

# a=56
# b=44
# mathoperation()

# Function with parameter/argument
    # Positional
    # Default
    # Keyword
    # Arbitrary positional
    # Arbitrary keyword

# Positional

# def empdetails(emp_name,emp_email,emp_location):
#     print("{} having email id as {} works at {} city".format(emp_name,emp_email,emp_location))

# empdetails('Rakib','rk@gmail.com','Hyderabad')

# Default

# def empdetails(emp_name,emp_email,emp_location='Hyderabad'):
#     print("{} having email id as {} works at {} city".format(emp_name,emp_email,emp_location))

# empdetails('Rakib','rk@gmail.com')

# Keyword

# def empdetails(emp_name,emp_email,emp_location):
#     print("{} having email id as {} works at {} city".format(emp_name,emp_email,emp_location))

# empdetails(emp_email="abc.gmail.com",emp_location="Hyderabad",emp_name="Rakib")

# Arbitrary positional

# def transactions(*a):
#     # print(a)
#     deduct_amount=0
#     for j in a:
#         deduct_amount = deduct_amount + j

#     print("{} amount has been dedcuted".format(deduct_amount))

# transactions(243,564,765.43,456,178.90)
# transactions(7484,345)

# Arbitrary keyword

# def transactions(**a):
#     # print(a)
#     for j in a:
#         print("In {}, you have spent {}".format(j,a[j]))

# transactions(January=2450,February=4638,March=8934)

# return statements
    # print just display the o/p, return can store o/p and send it to another function call
# def addition(a,b):
#     return (a+b)*(a*b)

# def substract(c):
#     # print(addition(4,5)-c)
#     return (addition(4,5)-c)

# # substract(3)

# def multiplication(d):
#     return (substract(7)*d)

# print(multiplication(2))

# Recursion : Function calling itself

# factorial calculation

# def fact_cal(a):
#     if a==1:
#         return 1
#     else:
#         return a*fact_cal(a-1)

# print(fact_cal(6))

# global & local variable
    # local variable : declared inside function and can be accessed inside function only
    # global variable : declared outside of function and can be accessed anywhere in program/module

# a=45

# def addition(a,b):
#     print("Inside a value", a)
#     print("Inside b value", b)

# print("Outside a value", a)

# addition(5,6)

# print("Outside a value", a)

# lambda function (function without name)

# syntax : lambda arguments:expression

# def sample(a):
#     return a*2

# print ((lambda a:a*2)(3))
# print ((lambda a,b,c:a*b*c)(3,4,5))

# b=[]
# def sample(a):
#     for j in range(1,a+1):
#         if j%2==0:
#             b.append(j)
#     return b

# print(sample(10))

# map : looping in lambda

# print(list(map(lambda j:j*2,range(1,11))))

# filter : looping with condition in lambda

# print(list(filter(lambda j:j%2==0, range(1,11))))