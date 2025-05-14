#multithreading 
import threading
import time

def print_number():
    for i in range(5):
        time.sleep(1)
        print(f"Number:{i}")

def print_letter():
    for letter in'abcde':
        time.sleep(1)
        print(f"Letter:{letter}")

"""
t = time.time()
print_number()
print_letter()
print(f"Time taken: {time.time()-t}")
"""

#creating a 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()
#start threads
t1.start()
t2.start()

t1.join()
t2.join()

print(f"Time taken: {time.time()-t}")