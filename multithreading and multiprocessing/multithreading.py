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


t=time.time()
print_number()
print_letter()
print(f"Time taken: {time.time()-t}")
