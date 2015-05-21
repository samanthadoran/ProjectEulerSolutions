#include <iostream>
#include <time.h>
#include <vector>
using namespace std;

//Find L(S)
unsigned long long int sequential(vector<bool> num)
{
	bool currNum = false;
	unsigned int currSeq = 0;
	unsigned int maxSeq = 0;

	//Loop through our data
	for(int i: num)
	{
		//The number has changed
		if(i != currNum)
		{
			//Is the current sequence bigger? If so, reset maxSeq
			if(maxSeq < currSeq)
				maxSeq = currSeq;
			
			//Reset currSeq and currNum to reflect the change
			currNum = i;
			currSeq = 1;

			/*Is there even a chance of a longer sequential subsequence?
			If not, just break.*/
			if((num.size() - i) <= maxSeq)
				break;
		}
		else
		{
			//The number is the same, continue and increment
			++currSeq;
		}
	}

	//Perform the last check out of the loop...
	if(currSeq > maxSeq)
		maxSeq = currSeq;

	return maxSeq;
}

//unsigned long long int recursive(bool * num, unsigned int base, int index)
unsigned long long int recursive(vector<bool> num, int index)
{
	//Root case
	if(index == (num.size() - 1))
		return sequential(num);

	/*The special case occurs when the next index is equivalent to current one
	as it extends the current sequence*/
	num[index + 1] = num[index];
	unsigned long long int special = recursive(num, index + 1);

	/*The regular case occurs when the number is anything but the previous index,
	thus breaking the current sequence*/
	num[index + 1] = !num[index];
	unsigned long long int regular = (num.size() - 1) * recursive(num, index + 1);

	return special + regular;
}

int main()
{
	//Track the start time...
	time_t t1;
	time(&t1);

	//Get the size of our n-sequence
	unsigned int base;
	cout << "Enter the length of S" << endl;
	cin >> base;

	/*Initialize our data, using booleans because we only care if numbers are
	the same or not, so ones and zeros do nicely*/
	vector<bool> number;

	//Assign our number to a base case
	for(int i = 0; i < base; ++i)
		number.push_back(true);

	//Run the algorithm
	unsigned long long int L = base*recursive(number, 0);

	//Track the end time
	time_t t2;
	time(&t2);

	std::cout << "Done, the answer is: " << L << std::endl;
	
	std::cout << "Runtime was " <<difftime(t2,t1) << std::endl;

	return 0;
}