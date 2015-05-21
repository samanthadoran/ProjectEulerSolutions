def primeFactorize(k):
	factors = []

	pow = 0
	while k % 2 == 0:
		pow+=1
		k/=2

	factors.append((2,pow))

	pow = 0
	for i in range(3, int(k**.5 +1)):
		while k % i == 0:
			pow+=1
			k/=i
		factors.append((i,pow))

	if k > 2:
		factors.append((k,1))

	return factors



def main():
	factors = []
	multipliers = []

	#Get tuples of our prime factorizations...
	for i in range (1,21):
		factors+=(primeFactorize(i))
	
	#We only want one of each term, it should have the highest power...
	for i in factors:
		for j in factors:
			#These have the same base...
			if i[0] == j[0]:
				#The exponent of i is less, we should make i equivalent to j to fix this.
				if i[1] < j[1]:
					i = j

		#We don't want duplicates.
		if not i in multipliers:
			multipliers.append(i)

	num = 1

	for i in multipliers:
		num*=i[0]**i[1]
	
	print(num)

if __name__ == '__main__':
	main()