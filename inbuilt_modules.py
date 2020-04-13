# Inbuilt modules
    # Random/datetime/calendar/os/urllib etc.

# import random

# # print(dir(random))
# # print(random.random()) # getting random floating value between 0 & 1
# # print(random.randint(1000,9999)) # int value between given range

# a=['Coupon1','Coupon2','Coupon3','Coupon4']

# # print(random.choice(a)) # pick a choice randomly
# random.shuffle(a) # Shuffle it random way
# print(a)

# import datetime
# # print(dir(datetime))
# # print(dir(datetime.date))
# # print(datetime.datetime.today())
# # print(datetime.datetime.today().date())
# # print(datetime.datetime.today().date().month)
# # print(datetime.datetime.today().time())
# # print(datetime.datetime.today().time().hour)
# # print(datetime.datetime.today()+datetime.timedelta(days=45))
# print(datetime.datetime.today()+datetime.timedelta(minutes=60))

# import calendar

# print(calendar.month(2020,12))
# print(calendar.isleap(1996))
# print(calendar.day_name[2])
# print(calendar.weekday(2020,4,2))

# import os

# print(os.getcwd()) # to get current working directory
# os.chdir("<directory name>") # to change the directory
# print(os.listdir(".")) # list all file/folder inside the current directory

# print(os.path.isfile("C:/Users/Kaniz-pc/OneDrive/Documents/PythonClass")) # To check whether given path is file

# # os.mkdir("Test1") # To create a new folder
# os.rmdir("Test1") # To remove an existing folder

# os.makedirs("<Internal folder path>") # to create internal folders
# os.removedirs("<Internal folder path>") # to remove internal folders


# import urllib.request

# url_data = urllib.request.urlopen("https://www.google.com/")
# # print(url_data)
# print(url_data.read())

# # bs4 : beautifulsoup4 (module for scraping the details)

# External Module : those which we download externally based on requirement

# pip : python package manager (to install modules for python)

# pip install <package-name>
    # ex: pip install numpy

# pip list : will list all packages that are downloaded externally