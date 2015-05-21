from itertools import *
import time

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

#This function returns a list of all possible permutations of x
def pandigitals(x):
	#First, we need a list
	toRet = []

	'''
	Annoyingly enough, or not annoying, it makes tuples of it so.. "abc" yields
	("a","b","c"),("b","c","a")... So, loop over the results and then add the 
	contents of each element of each tuple to a string to be appended to our 
	return list.. So, ("a","b","c") becomes "abc" and is appended.
	'''
	for i in permutations(x, len(x)):
		toAdd = ""
		for j in i:
			toAdd += j
		toRet.append(toAdd)
	#Return our list of len(x) digit pandigital numbers...
	return toRet

def main():
	t1 = time.time()
	numbers = []
	
	#We only care about [2,9] digit numbers...
	for n in range(2,10):
		toPass=""
		#Create the base case, i.e. a 5 digit pandigital becomes 12345
		for j in range(1,n+1):
			toPass+=str(j)
		#Pass our base case to pandigitals to get all of the possible pandigitals
		numbers.append(pandigitals(toPass))
	
	primes = []
	
	#Now, numbers is now a list of lists, so we must loop over it as such
	for i in numbers:
		for k in i:
			#Test if numbers[i][k] is prime, add it to the list if it is
			if isPrime(int(k)):
				primes.append(int(k))

	#Print out the largest!
	print(max(primes), time.time()-t1)

if __name__ == "__main__":
	main()