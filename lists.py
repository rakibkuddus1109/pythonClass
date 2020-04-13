# Lists : sequence of multiple elements which are separated by comma, declared inside [].
    # Example: [2,'Python',6.7,[11,12,'Test']]
    # Nested list : List declared inside a list
    # List is mutable
    # print(dir(list)) : To get methods available for list

# Accessing the element inside list: Indexing

# a=[2,'Python',6.7,[11,12,'Test']]
# # print(a[3])
# # print(a[1:4])
# # print(a[0:4:2]) # slicing, it is going to get 0 to 4 index, jumping by 2 position
# # print(a[-1])
# print(a[3][2]) # Nested Indexing

# Mutability
# a=[2,'Python',6.7,[11,12,'Test']]
# print(a)
# a[2]=3.4
# print(a)

# append/extend/insert
    # append : for injecting single element at the end
    # extend : multiple element injection at the end (give any sequential datatype, number is not permitted)
    # insert : single element injection at any specified position

# append
# a=[2,'Python',6.7,[11,12,'Test']]
# a.append(11)
# a.append("Django")
# a.append([9,3.8,12])
# print(a)

# extend
# a=[2,'Python',6.7,[11,12,'Test']]
# a.extend([43,"Datascience",3.4]) # Separates each element from the list and injects
# print(a) # [2, 'Python', 6.7, [11, 12, 'Test'], 43, 'Datascience', 3.4]

# insert
# a=[2,'Python',6.7,[11,12,'Test']]
# a.insert(2,"Devops")
# print(a)

# remove : Would remove the element which is intended to be removed
# a=[2,'Python',6.7,[11,12,'Test']]
# a.remove(6.7)
# print(a)

# pop : Removes element based upon index value
# a=[2,'Python',6.7,[11,12,'Test']]
# # a.pop(1)
# # print(a)
# print(a.pop(1)) #Shows which element is getting removed

# clear : removes all elements from list and makes it empty
# a=[2,'Python',6.7,[11,12,'Test']]
# a.clear()
# print(a)

# index : To find index value of given element
# a=[2,'Python',6.7,23,28,"23"]
# print(a.index("23")) #returns for str 23
# print(a.index(23)) #Returns for int 23

# count : Returns no. of times a particluar element is present
# a=[2,'Python',6.7,[11,12,'Test'],16,16]
# print(a.count(16))

# sort : Sorting values in list, deafult is descending
# a=[34,8,45,9,92,87]
# # a.sort()
# a.sort(reverse=True) #ascending
# print(a)

# reverse : To reverse a list
# a=[2,'Python',6.7,[11,12,'Test']]
# a.reverse()
# print(a)

# copy : Copy the list to another variable with different memory allocation, further inclusion in parent one doesn't impact 
# a=[2,'Python',6.7,[11,12,'Test']]
# # b=a : this gives same memory allocation -- deep copy
# b=a.copy() #this also keeps same value as 'a' but memory allocation is different -- shallow copy
# print(id(a))
# print(id(b))
# a.append(57)
# print(a)
# print(b)

# # Task
# a=[23,"Python",'64',64,12,'12',12,23,"Django"] # Remove duplicate

# List Comprehension : Faster way to setup a list
    # Syntax: 
    # [expresssion for element in sequence]
# a=[]
# for j in range(2,20):
#     a.append(j)
# print(a)

print([j for j in range(2,20)])

# for any if-else condition (elif is not allowed in list comprehension)
# a=[]
# for j in range(2,20):
#     if j%2==0:
#         a.append(j)
#     else:
#         a.append(j*3)
# print(a)
print([j if j%2==0 else j*3 for j in range(2,20)]) # printing even number as-is and odd number multiplying by 3

a=["abc@fb.com","xyz@gmail.com","mno@gmail.com","dfg@ef.com"]
print([j for j in a if j.endswith("gmail.com")]) 

# in absence of else keep loop before condition
# in presence of both if/else keep loop after condition