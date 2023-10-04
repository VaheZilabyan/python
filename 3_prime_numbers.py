import time
import math

def is_prime(n):
    if n <= 1:
        return False;
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False;
 
    return True;

def prime_numbers():
    n = 2
    while True:
        if is_prime(n):
            print(n)
        n += 1
        time.sleep(0.1)

prime_numbers()