def nextFibPair(pair):
	y = pair[1]
	x = pair[0]
	
	temp = y
	y = x + y
	x = temp

	temp = y
	y = x + y
	x = temp

	return (x,y)

def evenAdd(pair):
	for i in pair:
		if i % 2 == 0:
			return i
	return 0

def main():
	sum = 0
	pair = 1, 2

	while(max(pair) < 4000000):
		sum += evenAdd(pair)
		pair = nextFibPair(pair)

	print(sum)

if __name__ == "__main__":
    main()