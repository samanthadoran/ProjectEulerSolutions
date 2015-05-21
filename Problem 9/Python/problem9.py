def main():
	 for a in range(1,1000):
	 	for b in range(1,1000):
	 		c = (a**2 + b**2)**.5
	 		if (c % 1 == 0) and (a + b + c == 1000):
	 			print(a,b,c)
	 			print(a*b*c)


if __name__ == '__main__':
	main()