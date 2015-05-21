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
	pFactor= 0
	factor = 3
	number = 600851475143
	while factor < number**.5 + 1:
		if number % factor == 0:
			#If it is prime, set the pFactor
			if isPrime(factor):
				pFactor = factor
		#Increment by two to skip all even numbers
		factor+=2
	print(pFactor)

if __name__ == '__main__':
	main()