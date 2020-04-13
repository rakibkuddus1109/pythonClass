# Tuples : Sequence of elements separated by comma declared inside () 
    # () is not mandatory but recommended to use
# a=(3,"4","Python",6.7)
# print(a)
# b=3,"4","Python",6.7
# print(type(b))
# c=(3,) # Single value tuple
# print(type(c))

# Accessing the element in tuple : Indexing
# a=(3,"4","Python",6.7)
# print(a[2])
# print(a[0:4])
# print(a[0:5:2]) # Slicing
# print(a[::-1])

# Tuple elements are immutable, if element is declared as mutable datatype, addition of element there is possible

# a=(23,"Python",5.6,[11,13,12])

# Only supported for tuple -- index, count
# print(dir(tuple))

# Index: Giving index value of particular element
# Count : Retunrs how many times a element is present in tuple
# print(a.count(23))

# Looping in tuple
# a=('Python',23,56.78,'Django',12)

# for j in a:
#     if type(j)==str:
#         print(j)


# Basic operation on tuple:
    # Concatenation : Adding 2 or more tuples
    # Repetition : Repeating same tuple multiple times

a=(1,2,3,4)
b=("Python","Django","Datascience")
print(a+b)

print(a*4)

# Task:
# a is a tuple
# Calculate sum of all even number in a and keep it in another tuple b
# Calculate sum of all odd number in a and keep it in tuple c