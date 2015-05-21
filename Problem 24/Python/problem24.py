from itertools import *

def main():
	stuff = "0123456789"
	x = []
	for i in permutations(stuff, len(stuff)):
		x.append(i)
	print(x[1000000-1])

if __name__ == "__main__":
	main()