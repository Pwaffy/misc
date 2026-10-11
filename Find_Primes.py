# Find primes with threads

import sympy
import threading
import time

lock = threading.Lock()

primes = []

def findprimes(a, max):
    start = time.time()
    primess = []
    for i in range(max+1):
        if i % 4 == a:
            if sympy.isprime(i):
                primess.append(i)
    with lock:
        primes.extend(primess)
    end = time.time() - start
    with lock:
        print(f"Total execution time of thread {a}: {end}")


yum = input("number: ")
# yum = 100000


for i in range(4):
    t = threading.Thread(target=findprimes,args=(i,int(yum)))
    t.start()
    t.join()
# primes.sort()
# print(primes)