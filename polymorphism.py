# polymorphism : Many ways to define the method
    # Method overloading
    # Method overriding

# Method overloading: Considering relevant methods based upon no. of arguments that method has
# even though the method names are same

# Python doesn't support method overloading

# class Operation:

#     def mul(self,a,b,c):
#         return (a+b)*(a-c)
#     def mul(self,a,b):
#         return a*b

#     # def mul(self,a,b,c):
#     #     return (a+b)*(a-c)

# obj = Operation()

# print(obj.mul(4,5))


# Method overriding: Considering the child class method even though parent class method is present

class First:
    def add(self,a,b):
        return a+b

class Second(First):
    def add(self,a,b):
        return a*b

obj = Second()

print(obj.add(5,6))