#A function to test the primality of a given number...
def is_prime(k):
	factors = 0
	#We only really care about [1,sqrt(k)+1]
	for i in range(1, int(k**.5 + 1)):
		#i is a factor of k
		if k % i == 0:
			factors+=1
		#We aren't prime
		if factors >= 2:
			return False
	#Prime!
	return True

#A function to list the primes below n
def list_primes(n):
	primes = []
	primes.append(2)

	#All primes are odd (sans 2)...
	for i in range(3,n,2):
		if is_prime(i):
			primes.append(i)

	return primes


def main():
	primes = []
	primes = list_primes(10)
	
	print(sum(primes))


if __name__ == '__main__':
	main()