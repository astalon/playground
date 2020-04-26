'''

Author: Erik Lagerström

This program implements the Sieve of Eratosthenes, finding all primes up to a certain number in an efficient manner

'''

import time
import math

N = 1000000
	
def is_prime(number):
	if number == 2: return True

	for i in range(2, int(math.ceil(number**0.5))+1):
		if number%i == 0: return False
	return True

def soe(N):

	primes = [True for i in range(N)]

	primes[0] = False
	primes[1] = False

	p = 2

	while p*p <= N:

		if primes[p]:
			for i in range(2, int(math.ceil(N/p))):
				primes[p*i] = False

		p += 1
	print(primes.count(True))




def naive(N):
	prime_list = []
	is_prime_calls = 0

	for i in range(2, N):
		if is_prime(i):
			prime_list.append(i)
	
	print(len(prime_list))


soe(N)
naive(N)

