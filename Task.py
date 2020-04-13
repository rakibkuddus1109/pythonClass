# num=int(input("Enter the number:"))
# # count = 1
# # for j in range(2 , num + 1):
# #     while count < j:
# #         k = j ** j
# #         count = count + 1
# #         a = ("%d" %j)
# #         for i in range(1 , j):
# #             a = a + (" * %d" %j)
# #         print(a, "=", k)

# for j in range (2,num + 1):
#     # print((("{}*".format(j))*j).rstrip("*"), "=", j**j)
#     # print((("{}*".format(j))*j)[0:-1], "=", j**j)
#     print("*".join(("{}".format(j))*j), "=", j**j)

# # List Task:
# a=[23,"Python",'64',64,12,'12',12,23,"Django"]
# b=[]
# # for i in range(len(a)) :
# #     if a[i] not in b:
# #         b.append(a[i])
# # print(b)
# print(b.append(a[j]) for j in range(len(a)) if a[j] not in b)

# Dict task
a={}
n=int(input("Enter number of data that you want to enter: "))
for j in range(1,n + 1):
    name = input("Enter Name: ")
    dob = input("Enter DOB: ")
    if name in a:
        a[name]=a[name]+(dob,)
    else:
        a[name]=(dob,)

print(a)