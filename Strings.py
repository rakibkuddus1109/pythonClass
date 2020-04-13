# Strings: Sequence of anything declared inside "" or ''

# a="Python Class @ Digital Lync" # Single line string
# b='Python Class @ "Digital Lync"'
# c="Python Class @ 'Digital Lync'"
# d='''Python Class
#     @ Digital Lync''' # Multi line string
# print(a,b,c,d)

# Accessing elements inside string : indexing
# Indexing starts from zero, goes till length of the string
# Negative indexing is also there and it starts from -1

# a="Python is a programming language"
# print(a[12]) # For single element
# print(a[12:19]) # Access range of elements
# print(a[0:19:3]) # Slicing
# print(a[18:11:-1]) # In reverse order -- Negative indexing (offset is mandatory which is negative)
# print(a[-10]) # Negative Indexing
# print(a[-14:-21:-1])
# print(len(a)) # calculates the length -- here it is 32
# print(a[-1:-(len(a)+1):-1]) # Give 1 more negative to length, i.e. -33
# print(a[::-1]) # Another way to reverse entire string

# Mutable : List, Dictionary, Sets
# Immutable : String, Number, Tuple

# So strings are immutable

# a="Python"
# a[0]="p" # This is not possible to update as it's immutable

# Basic operations on string:
    # Concatenation (+) : Addition of two or more string
    # Repetition (*) : Repeating same string 'n' number of times

# a="Python"
# b="Datascience"

# print(a+b)
# print(a*4)
# print(b*2)

# Methods of string
# print(dir(str)) # To print different available method
# print(help(str)) 

# Mostly used methods: startswith, endswith, upper, islower, isupper, capitalize, isdigit and so on

# a="django is a web based framework"
# b=["dinesh","divakar","chakra","chitti"]

# startswith() : Checks whether string starts with specified substring

# for j in b:
#     if j. startswith('d'):
#         print(j)

# endswith() : Checks whether string ends with specified substring 

# islower() : For checking whether all alphabtes are in lower case

# a="Django is frameWORK 123"
# b="all are lower case"
# print(a.islower())
# print(b.islower())

# isupper() : Checks whether all alphabets are in upper case

# isalpha() : Checks whether all elements in string are alphabets only
# a = "Python 123 Test"
# print(a.isalpha())

# isalnum() : Checks whether all elements in string are alphanumeric

# isdigit() :  Checks whether string contains numbers only

# lower() : Converting whole strings in lower case
# upper() : Converting whole strings in upper case
# a="UPPerCase"
# b ="lowercase"
# print(a.lower())
# print(b.upper())

# capitalize() : Converts starting character of string in upper case and rest in lower
# a="django is FRAMEWork"
# print(a.capitalize())

# title() : Evry word starting character in string would be converted in upper case
# a="python is programming language"
# print(a.title())

# swapcase() :  Swapping upper case to lower & vice versa

# index() : For finding index value of a character in a string (stops execution of program if index not found)
# a="Testing index"
# print(a.index('i'))

# count() : To count occurance of and element in string
# print(a.count('i'))

# find() : For finding index value but it doesn't stop program but keeps continued if not found

# replace() : 
b="don't trouble the trouble trouble will trouble you"
print(b.replace('trouble','problem'))
print(b.replace('trouble','problem',2)) #only for specifed occurance as mentioned in 3rd one

# split() : To split string into list, returns output as list
# a="Python is programming language"
# # print(a.split())
# print(a.split("a"))

# strip() : For removing escape sequence & spaces at the end from both side of string

a="\nPython is a language\n\tDjango is a \tframework\n" #\n:new line,\t:tab space
print(a.strip())

# lstrip() : For removing escape sequence & spaces at starting of string
# rstrip() : Reverse of lstrip

# zfill() : Prefixing string with zeroes
a="8796461"
print(a.zfill(15))

# join() : to add any char between elements in string
# a="python"
# print("-".join(a))
a="python is used for web development"
b=a.split()
print(b)
print("-".join(b))

# .format()
emp_id=int(input("Enter Emp Id:"))
emp_name=input("Enter Emp Name:")
emp_company=input("Enter company name:")
# print("{} having empid {} works for {} company".format(emp_name,emp_id,emp_company))
# print("{1} having empid {2} works for {0} company".format(emp_company,emp_name,emp_id))
print("{name} having empid {eid} works for {comp} company".format(comp=emp_company,name=emp_name,eid=emp_id))

# Task:
# User has to enter a number
# It should go upto that number multiplying by same number
# example: if User gives 4, below should happen
# 2*2=<result>
# 3*3*3=<result>
# 4*4*4*4=<result>