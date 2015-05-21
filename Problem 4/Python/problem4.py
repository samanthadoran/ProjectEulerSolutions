def main():
	palindromic = []
	for i in range(100,1000):
		for j in range(100,1000):
			if str(j*i) == str((j*i))[::-1]:
				palindromic.append(j*i)
	print (max(palindromic))

if __name__ == "__main__":
	main()