# Module : Every python is called as module
    # User defined : .py file created by user
    # Inbuilt : .py file comes with pyhton by default
    # External libraries : installed from external sources

# Syntax for module:
"""import <module name>"""

# module name : python file name that is to be used

# import module_1
# import module_2
# print(module_1.add(6,7))

# print(module_2.username)

# print(module_2.add(5,6,7))

# from module_1 import *
# from module_2 import *  # considers latest import
# print(add(6,7)) # This step would give error
# print(add(5,6,7))

# Python checks at 3 locations while importing any module
    # Current working folder
    # location where python is installed
    # location where python environment variable is set

# import sys
# print(sys.path)

# # To add a new path : sys.path.append(<your path>)

# print(help('modules')) # fetch all modules present on the system