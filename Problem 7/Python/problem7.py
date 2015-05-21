#A function to test the primality of a given number...
def isPrime(k):
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

def main():
	numPrimes = 1
	prime = 2
	num = 3

	while numPrimes < 10001:
		if isPrime(num):
			numPrimes+=1
			prime = num
		num+=2
	print(prime)

if __name__ == '__main__':
	main()