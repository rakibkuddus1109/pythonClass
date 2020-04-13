# File operation : Reading/writing/appending file
# type of files : .txt/.py/.csv/.xlsx/.json etc.

# 2 ways to open file
    # 1st way -- variable = open("<path of file>",'<mode to open>')
        # mode to open : read (r), write (w), append (a)
    # 2nd way -- with open("<path of file>",'<mode to open>') as object:
    #                 Statements 

# file = open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\Sample_1.txt",'r')
# print(file)
# file.close() # have to manually close it
# print(file.closed)


# with open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\Sample_1.txt",'r') as file:
#     print(file)

# print(file.closed) # No need to clsoe the file separately, it would be closed once outside of statements

# Reading file -- r
    # read : reads everything inside the file, reading is performed by one entity at a time
    # readline : can read one line at a time from beginning, reading happens by one entity/character at a time
    # readlines : can read all lines inside file, read is perfomred by line

# with open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\Sample_1.txt",'r') as file:
    # print(file.read())
    # for j in file.read():
    #     print(j)

    # print(file.readline())
    # for j in file.readline():
    #     print(j)

    # print(file.readlines())
    # for line in file.readlines():
    #     print(line)

    # for line in file.readlines():
    #     if "Python" in line:        # To print only lines with specified item
    #         print(line)

    # print(file.readlines()[3]) # To print a specific line with line number

    # read_line = file.readlines()
    # for line in read_line:
    #     if "Python" in line:
    #         print(read_line.index(line))

# Writing file -- w : overwrites previous content & add newly given ones (if given file doesn't exist, it creates)
    # write : For writing only 1 string content at a time
    # writelines : can write n number of line of content, take input as list

# with open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\Sample_1.txt",'w') as file:
#     # file.write("This is by write operation")
#     file.writelines(["Python is a programming language\n","Django is a framwork\n","This write is through writelines"])

# Appending file -- a : rest operation is same as write/writelines

# with open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\Sample_1.txt",'a') as file:
#     # file.write("\nNow this is an append operation")
#     file.writelines(["\nPython is a programming language\n","Django is a framwork\n","This write is through writelines"])


# CSV : Comma separated values (Python has inbuilt module 'csv' for handling CSV file)

import csv

# reading

# with open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\std_details.csv",'r') as file:
#     csv_reader = csv.reader(file)
#     # print(csv_reader)
#     next(csv_reader) # to skip header in file
#     for row in csv_reader:
#         # if row[0] == 'Rakib':
    
#             print(row)

# writing

# with open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\std_details_1.csv","w",newline="") as file:
#     csv_writer = csv.writer(file)
#     # csv_writer.writerow(["std_name","email","phone"])
#     # csv_writer.writerow(["Rakib","rk@gmail.com","8099319336"])
#     csv_writer.writerows([["std_name","email","phone"],["Kaniz","rk@gmail.com","8099319336"],["Rafaat","rk@gmail.com","8099319336"]])

# appending

# with open("C:\\Users\\Kaniz-pc\\OneDrive\\Documents\\PythonClass\\std_details_1.csv","a",newline="") as file:
#     csv_writer = csv.writer(file)
#     # csv_writer.writerow(["std_name","email","phone"])
#     # csv_writer.writerow(["Rakib","rk@gmail.com","8099319336"])
#     csv_writer.writerows([["Rakib","rk@gmail.com","8099319336"],["Neo","rk@gmail.com","8099319336"]])

# Task:

# 1st txt file : a=5
# 2nd txt file : b=67
# 3rd txt file : c=a-b (perform the operation & write it in new line)

# Take a csv file with student details (name/email/mobile no)
# Take a user input to specify which column to take for filtering (e.g.: mobile no)
# element to search for filtering (e.g.: number starts with 8)
# write the result in a separate csv file