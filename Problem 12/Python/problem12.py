import time

def triangle_num(k):
	return int(k*((k+1)/2))

def factors(n):
	while n > 1:
		for i in range(2, int(n + 1)):
			if n % i == 0:
				n /= i
				yield i
				break

def make_tup_list(factorList):
	newfactors = [()]
  
	for i in factorList:
		count = 0
		for j in factorList:
			if j == i:
				count+=1

		itContains = False
		for j in newfactors:
			if i in j:
				itContains = True
				break;

		if not itContains:
			newfactors.append((i,count))

  return newfactors

def num_divisors(k):
	factorList = []

	#Prime factorize k...
	for factor in factors(k):
		factorList.append(factor)

	#Get tuples of the factors a raised to power b (a,b)
	factorList = make_tup_list(factorList)
  
	divisors = 1
  
	#The number of factors we have is (a+1)*(b+1)*(c+1) where a, b, and c are the powers in the prime factorization
	for i in factorList:
		if i != ():
			divisors *= i[1]+1

	return divisors

def main():
	t1 = time.time()
	i = 1
	while num_divisors(triangle_num(i)) < 500:
		i+=1
	print(triangle_num(i), time.time()-t1)


if __name__ == '__main__':
	main()