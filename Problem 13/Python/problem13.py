import math

def get_digit(num, index):
	tmp1 = (num // 10**index);
	tmp2 = (int(tmp1//10))*10;    
	return tmp1 - tmp2; 

def main():
	f = open('input.txt', 'r')
	sum = 0

	#With slicing...
	for line in f:
		sum += int(line)
	print(str(sum)[0:10])
	
	#Without slicing...
	digits = int(math.log10(sum))+1
	store = ''
	for i in range(digits - 1 , digits - 11, -1):
		store += str(get_digit(sum,i))
	print(store)

if __name__ == '__main__':
	main()