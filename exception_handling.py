# Exception Handling: Handling the exception or error

    # In-built exception : comes with programming language itself
    # User-defined exception : setting up our own defined exception

# In-built exception:

# a = [6,5.6,'Python',0,67]

# for j in a:
#     print(1/j)  # this would give in-built exception when 'Python' would come for division

"""
try:
    <statement>
except:
    <statement>
"""

# try : those lines which may give an error, has to be written inside 'try' block
# except : statements which should be executed after error occurance, comes under 'except' block

# 'try' block should have minimum one 'except' block

# import sys  # importing to know the type of error
# a = [6,5.6,'Python',0,67]
# a = [6,5.6,'Python',0,67,(12,23)]

# for j in a:
#     try:
#         print(1/j)
#     # except:
#     #     print("Error has occured for",j,sys.exc_info()[0])
#     except TypeError:
#         print("You have tried to divide with different type of data")
#     except ZeroDivisionError:
#         print("You are trying to divide by 0")
#     except:
#         print("Undefined error has occured!")

# print("Execution is over.")


# User-defined exception:

class ValueSmallError(Exception):   # Inherit "Exception" class to make it as an exception class
    pass

class ValueLargeError(Exception):
    pass


num1 = int(input("Enter num1 value:"))

while True:
    try:
        num2 = int(input("Enter num2 value:"))
        if num2 < num1:
            raise ValueSmallError  # to call exception class use "raise"
        elif num2 > num1:
            raise ValueLargeError
        else:
            print("Number guessed correctly!")
            break
    except ValueSmallError:
        print("Value entered is smaller, try again!")
    except ValueLargeError:
        print("Value entered is larger, try again!")