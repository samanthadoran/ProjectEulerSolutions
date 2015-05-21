import time

#Find L(S)
def sequential(num, base):
	currNum = 0
	currSeq = 0
	maxSeq = 0

	#Loop through our number...
	for i in range(0, base):
		#If the number is different...
		if currNum != num[i]:
			#Check the currSeq against maxSeq, assign accordingly
			if maxSeq < currSeq:
				maxSeq = currSeq

			#Reset the currNum and currSeq
			currNum = num[i]
			currSeq = 1

			#There isn't enough room for a sequence to be longer, just break.
			if (base - i) <= maxSeq:
				return maxSeq
		
		#If the number is the same...
		else:
			#Increment the currSeq
			currSeq += 1

	#Do this last check outside of the loop, no point in checking every run.
	if currSeq > maxSeq:
		maxSeq = currSeq
	
	return maxSeq

'''
Each index requires a special case and a regular case.
For each instance of index -1, you need a new special and regular case
'''
def recursive(num, base, index):
	#Root case
	if index == (base - 1):
		return sequential(num, base)
	
	#The special case occurs when the next index is equivalent to current one (so the left hand sequence can be longer)
	num[index + 1] = num[index]
	special = recursive(num, base, index + 1)
	
	#The regular case is anything else but above, so there are base-1 occurences of it
	num[index + 1] = 1 + num[index]
	regular = (base - 1) * recursive(num, base, index + 1)

	return special + regular


def main():
	#t1 = time.time()
	
	#Our base represents how high we can go
	number = []
	base = 4
	
	#Make a list to work with our number
	number.append([])
	for i in range(0, base):
		number[0].append(1)

	print(base * recursive(number[0], base, 0))#, time.time() - t1)
	#print("Time in seq", timeInSeq)

	input()

if __name__ == "__main__":
	main()
