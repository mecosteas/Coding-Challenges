"""
Find all primes from 0 to N
Ex: Given N = 15, return 2, 3, 5, 7, 11, 13
"""


# O(N*log(log(n)): N time to mark as composite * the harmonic progression of the sum of primes
# It's difficult to prove if we don't know how to get the taylor series of this harmonic series
# The sieve works by getting marking all composite numbers as not prime and leaving all primes umarked
def sieve_of_eratosthenes(N):
    # make a list of all numbers from 0 to N and mark all of them as primes until proven otherwise
    primes = [True] * (N + 1)  # N + 1 because we're including 0
    # mark 0 and 1 as not primes
    primes[0] = primes[1] = False
    p = 2
    while p * p < N:
        if primes[p] == True:
            # mark every multiple of p as a composite number by looping in steps of p
            for i in range(p * p, N + 1, p):
                primes[i] = False
        p += 1

    for i in range(N + 1):
        if primes[i]:
            print(i, end=' ')


print('Sieve of Erastosthenes')
sieve_of_eratosthenes(15)


# Naive solution
def is_prime(n):
    # This can be improved a bit by checking only from 2 to sqrt(n)
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primes(N):
    for i in range(2, N):
        if is_prime(i):
            print(i, end=' ')


print('\nNaive solution')
get_primes(15)
