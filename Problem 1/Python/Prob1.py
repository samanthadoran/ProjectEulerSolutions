def sum(k):
	sum = 0
	for i in range(1, k):
		if (i % 3 == 0) or (i % 5 == 0):
			sum+=i
	return sum

def main():
	x = int(input("What's the number? "))
	print("The answer is: ", sum(x))

if __name__ == "__main__":
    main()