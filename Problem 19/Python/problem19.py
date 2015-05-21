import time
def main():
	t1 = time.time()
	months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	monthsLeap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	year = 1901
	count = 0
	weekday = 2
	isLeap = False

	#If day is 1, it is a sunday
	while year < 2000:
		if year % 4 == 0 or year % 400 == 0:
			isLeap = True
		else:
			isLeap = False

		if not isLeap:
			for j in range(1,13):
				for k in range(1,months[j] + 1):
					#print(str(j) +"/"+ str(k) +"/"+ str(year))
					if k == 1 and weekday == 1:
						count += 1
					if weekday + 1 > 7:
						weekday = 1
					else:
						weekday += 1
		else:
			for j in range(1, 13):
				for k in range(1, monthsLeap[j] + 1):
					#print(str(j) +"/"+ str(k) +"/"+ str(year))
					if k == 1 and weekday == 1:
						count += 1
					if weekday + 1 > 7:
						weekday = 1
					else:
						weekday += 1
		year += 1
	print(count, time.time() - t1)

if __name__ == '__main__':
	main()