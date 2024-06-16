import time
from math import sqrt
#time complexity sieve of eratosthenes is O(nloglog(n))
def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, max_num + 1):
        if is_prime[p]:
            prime_numbers.append(p)
    return prime_numbers

#this has time complexity of O((n)sqrt(n)) and might be fast in interview question
def is_prime(n):
    prime_flag = 0
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False

def find_prime_pair1(n):
    if n < 3:
        return [-1, -1]

    for a in range(2, n // 2 + 1):
        b = n - a
        if is_prime(a) and is_prime(b):
            return [a, b]
    
    return [-1, -1]

# Example Usage:
start = time.time()
n = 2234
result = find_prime_pair1(n)
end = time.time()
print(f"execution time : {(end-start)* 10**3}ms result of sqrt: {result}") # Output should be a pair of primes [a, b] such that a + b = n


def find_prime_pair(n):
    if n < 3:
        return [-1, -1]

    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)
    
    for a in primes:
        b = n - a
        if b in prime_set:
            return [a, b]
    
    return [-1, -1]

# Example Usage:
start = time.time()
n = 2234
result = find_prime_pair(n)
end = time.time()
print(f"execution time : {(end-start)* 10**3}ms result of Sieve: {result}")  # Output should be a pair of primes [a, b] such that a + b = n


