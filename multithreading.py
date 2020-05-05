import time
import threading
a = [2,3,4,5]

def square(a):
    for j in a:
        time.sleep(0.5)
        print(j**2)

def cube(a):
    for j in a:
        time.sleep(0.3)
        print(j**3)

t = time.time()
# square(a)
# cube(a)

t1 = threading.Thread(target=square,args=(a,))
t2 = threading.Thread(target=cube,args=(a,))

t1.start()
t2.start()

# join : when one process is in sleep mode, other would come & join

t1.join()
t2.join()

print("Execution time",time.time() - t)