from concurrent.futures import ThreadPoolExecutor
import time

def print_number(i):
        time.sleep(1)
        print(f"Number:{i}")

i=[0,1,2,3,4]

with ThreadPoolExecutor(max_workers=2) as executor:
        results=executor.map(print_number, i)

for result in results:
        print(result)