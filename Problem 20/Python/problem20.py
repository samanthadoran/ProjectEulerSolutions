from math import *

def main():
	sum = 0
	for i in str(factorial(100)):
		sum += int(i)
	print(sum)

if __name__ == "__main__":
	main()