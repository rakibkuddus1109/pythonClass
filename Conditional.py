# Conditional statement : Statement executed based upon certain condition
    # If statement
    # If-else statement
    # if-alif-else statement

# Indentation
# **if statement**
# if condition:
#     It is starting from here after 4 spaces, known as Indentation


# a=int(input("Enter a value:"))
# if a<50:
#     print("a is less than 50")

# print ("Condition not satisfied")

# **if-else statement**
# if condition:
#     statement
# else:
#     statement

# a=int(input("Enter a value:"))
# if a<50:
#     print(a,"is less than 50")
# else:
#     print(a,"is more than 50")

# pin1=int(input("Please enter pin code:"))
# if pin1==1234:
#     account_type=input("Enter Acount Type:")
#     if account_type=="Savings":
#         amount=int(input("Please enter amount to be withdrawn:"))
#         if amount<=20000:
#             print(amount,"is debited from your account")
#             print("Please collect your cash")
#         else:
#             print("Ammount should be less than or equal to 20000")
#     else:
#         print("You don't own this Account Type")
# else:
#     print("Invalid pin")


# **if-elif-else statement**
# if statement is mandatory to initiate this

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

Percentage=int(input("Enter your percentage:"))
if Percentage>=70:
    print("You got distinction")
elif Percentage>=60 and Percentage<70:
    print("You got 1st class")
elif Percentage>=50 and Percentage<60:
    print("You got 2nd class")
elif Percentage>=40 and Percentage<50:
    print("You are just passed")
else:
    print("Sorry you failed")