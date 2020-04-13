# Looping/Iteration: Executing certain set of statements multiple times
    # While Loop
    # For Loop
# While Loop: Continuous loop
"""
while condition:
    statements
"""

# a=int(input("Enter a value:"))

# if a>50:
#     print(a,"more than 50")

# print("-------")

# while a>50:
#     print(a,"more than 50")
#     a=a-1 # we have to make the condition false at somepoint hence decrementing it

# print("-------")
"""
Do Below Task using while loop
"""
# pin1=int(input("Please enter pin code:"))
# i = 0
# while i < 3:
#     pin1=int(input("Please enter pin code:"))
#     if pin1==1234:
#         # while i < 3:
#         account_type=input("Enter Acount Type:")
#         if account_type=="Savings":
#             amount=int(input("Please enter amount to be withdrawn:"))
#             if amount<=20000:
#                 print(amount,"is debited from your account")
#                 print("Please collect your cash")
#                 i = 4
#                 continue
#             else:
#                     print("Ammount should be less than or equal to 20000")
#                     i = i + 1
#         else:
#             print("You don't own this Account Type")
#             i = i + 1
#     else:
#         print("Invalid pin")
#         i = i + 1
# if i == 3:
#     print("Maximum Attempt reached for the day")
# else:
#     print("Have a good day!")

# For loop: Sequence Loop, except number all other datatypes in python are sequence
"""
for element in sequence:
    statements
"""

# a="Python is a programming language"
# a=[11,4.5,'Python','Django']
# for j in a:
#     # print(j)
#     print(j,end=" ")

# range: ex -- (1,17)

# for j in range (1,51):
#     print(j,end=" ")

# for j in range (51):
#     print(j,end=" ")

"""
Jump/Offset
"""
# for j in range (1,51,3):
#     print(j,end=" ")

# for j in range (50,0,-1):  #For reverse order negative jump has to be specified
#     print(j,end=" ")

# for j in range (-1,-51,-1):
#     print(j,end=" ")

# a=[]
# for j in range(1,6):
#     user_inp=int(input('Enter Input:'))
#     a.append(user_inp)
#     print(a)
# print(a)
# print(sum(a))

# for num in range(1,11):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num,"is a Prime Number")


# Control Flow Statements:
    # break : Stops iteration and comes out of loop
    # continue : Skips any next statement in loop and go back to next iteration
    # pass : for syntax purpose, not used as such.. mostly to execute empty block

# for j in range(2,100):
#     if j%2==0 and j%4==0 and j%8==0:
#         print(j, "Condition Satisfield")
#         # break
#         continue

a=24
if a%3==0:
    pass
