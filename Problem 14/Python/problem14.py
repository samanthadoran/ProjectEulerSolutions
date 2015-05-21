import time
def Collatz(k):
	i = 0
	while k != 1:
		if k % 2 == 0:
			k = k / 2
		else:
			k = 3*k + 1
		i+=1
	return i


def main():
	t1 = time.time()
	tup = (0,0)
	i = 2
	while i < 1000000:
		k = Collatz(i)
		if k > tup[1]:
			tup = (i,k)
		i += 1
	print(tup, time.time() - t1)

if __name__ == '__main__':
	main()