def main():
	lines = []
	f = open('input.txt', 'r')
	
	for line in f:
		lines.append(line)

	numbers = []

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

	toSave = []
	maxProd = 1
	
	#Left/Right
	for i in numbers:
		for j in range(0,len(numbers)-4):
			tmpProd = 1
			tmpSave = []
			for k in range(j, j + 4):
				tmpProd *= i[k]
				tmpSave.append(i[k])
			if tmpProd > maxProd:
				toSave = tmpSave
				toSave.append("left/right")
				maxProd = tmpProd

	#Up/Down
	for i in range(0,len(numbers[0])):
		for j in range(0,len(numbers)-4):
			tmpProd = 1
			tmpSave = []
			for k in range(j, j + 4):
				tmpProd *= numbers[i][k]
				tmpSave.append(numbers[i][k])
			if tmpProd > maxProd:
				toSave = tmpSave
				toSave.append("up/down")
				maxProd = tmpProd

	#Diagonal down to the Right
	for i in range(0,len(numbers[0]) - 4):
		for j in range(0, len(numbers) - 4):
			tmpProd = 1
			tmpSave = []
			for k in range(0,4):
				tmpProd *= numbers[i+k][j+k]
				tmpSave.append(numbers[i+k][j+k])
			if tmpProd > maxProd:
				toSave = tmpSave
				toSave.append("Diagonal down to the right")
				maxProd = tmpProd
	
	#Diagonal down to the left
	for i in range(0,len(numbers[0]) - 4):
		for j in range(3, len(numbers)):
			tmpProd = 1
			tmpSave = []
			for k in range(0,4):
				tmpProd *= numbers[i+k][j-k]
				tmpSave.append(numbers[i+k][j-k])
			if tmpProd > maxProd:
				toSave = tmpSave
				toSave.append("Diagonal down to the left")
				maxProd = tmpProd
	
	print(maxProd)
	print(toSave)
	f.close()

if __name__ == '__main__':
	main()