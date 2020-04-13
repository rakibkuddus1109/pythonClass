# Dictionary : Sequence of key:value pair separated with comma, declared inside {}
    # Ex: {"City":"Hyderabad","State":"Telangana"}

# Limitation:
    # All keys inside dictionary are immutable
    # Duplicate key declaration is not valid, it takes latest key:value pair for duplication

# a={1:"Python","City":"Hyd",(1,2,3):[4,5,6]}
# print(a)

# Accessing inside dictionary : Using key name
# a={"usename":"rk@abc.com","password":"rk123","email":"rk@abc.com"}
# print(a["email"])

# Dictionaries are mutable

# print(dir(dict))

# get :  For accessing key from dictionary, if key is not found, it returns 'None'
# a={"username":"rk@abc.com","password":"rk123","email":"rk@abc.com"}
# print(a.get('username'))

# adding key:value in dictionary
# a={"usename":"rk@abc.com","password":"rk123","email":"rk@abc.com"}
# a['Phone']='7653459081'
# print(a)

# update : For adding key:value pairs of a dictionary with another
# a={"usename":"rk@abc.com","password":"rk123","email":"rk@abc.com"}
# b={"company":"comp123","city":"Hyd"}
# a.update(b)
# print(a)

# Removal mehtods : 
    # pop() : For removing a specified key:value pair from dictionary
a={"usename":"rk@abc.com","password":"rk123","email":"rk@abc.com"}
# b={"company":"comp123","city":"Hyd"}
# a.update(b)
# print(a)
# a.pop("email")
# print(a)

    # popitem() : Removes last key:value pair by default from dictionary
# a.popitem()
# print(a)
# print(a.popitem()) # Shows which pair is removed

    # clear : Removes all key:value pair
# a.clear()
# print(a)

# keys() : To get all keys from dictionary
# print(a.keys())

# values() : Returns all values from dictionary
# print(a.values())

# items() : Returns key:value pair from dictionary
# print(a.items())

# fremkeys() : Dynamic creation of a dictionary with sequnce of values as keys
# a=["city","state","country","continent"]
# print({}.fromkeys(a,['Hyd'])) # This value would be assigned to all keys, can't assign different value for different key

# setdefault() : Giving a default value to particular key & append it in dictionary
# a={'city':'Hyd'}
# a.setdefault('State','Telangana')
# print(a)

# dictionary comprehension :
# {expression for elements in Sequence}

# b={}

# for j in range(1,10):
#     b[j]=j*2

# print(b)

print({j:j*2 for j in range(1,10)})
print({j:j*2 for j in range(1,10) if j%2==0}) # Syntax for only if statement
print({j:j*2 if j%2==0 else j*3 for j in range(1,10)}) # Syntax for if-else statement

# Task
# Ask user to enter name, DOB
# Ask same for 5 persons
# Give same name for 2 instances with different DOB
# Output should be like {'User1':('DOB1','DOB2'),'User2':('DOB1','DOB2'),'User3':('DOB')}