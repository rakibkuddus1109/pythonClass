import time
a = [2,3,4,5]

def square(a):
    for j in a:
        print(j**2)

def cube(a):
    for j in a:
        print(j**3)

t = time.time()
square(a)
cube(a)

print("Execution time",time.time() - t)