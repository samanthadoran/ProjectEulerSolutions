def walkTriangle(numbers, x, y, currSum):
	#Base case...
	if y == len(numbers) - 1:
		return currSum + numbers[y][x]

	#Add the number at our current position to the running sum
	currSum += numbers[y][x]

	#Which path is the greatest?
	return max(walkTriangle(numbers, x, y + 1, currSum), walkTriangle(numbers, x + 1, y +1, currSum))


def main():
	#Grab the lines and read them into a list...
	f = open('input.txt' , 'r')
	lines = []
	for line in f:
		lines.append(line)

	numbers = []
	
	#Split the lines into lists of lists of numbers
	for i in lines:
		tmpList = []
		tmpStr = ''
		for j in i:
			if j == ' ':
				tmpList.append(int(tmpStr))
				tmpStr = ''
				continue
			tmpStr += j
		tmpList.append(int(tmpStr))
		numbers.append(tmpList)

	#Slow recursive algorithm is slow.
	maxSum = walkTriangle(numbers, 0, 0, 0)

	print(maxSum)

	f.close()


if __name__ == '__main__':
	main()