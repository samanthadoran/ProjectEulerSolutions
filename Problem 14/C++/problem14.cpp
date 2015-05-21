#include <iostream>
#include <time.h>

unsigned int collatz(unsigned long int k)
{
	int i = 0;
	while(k != 1)
	{
		if(k % 2 == 0)
			k = k / 2;
		else
			k = 3*k + 1;
		++i;
	}
	return i;
}

int main()
{
	time_t t1;
	time(&t1);
	int savedNum = 0;
	int savedIter = 0;
	for(int i = 2; i < 1000000; ++i)
	{
		int k = collatz(i);
		if (k > savedIter)
		{
			savedIter = k;
			savedNum = i;
		}
	}
	time_t t2;
	time(&t2);
	std::cout << "(" << savedNum <<", " << savedIter << ")" << std::endl;
	std::cout << "Runtime was " <<difftime(t2,t1) << std::endl;
	return 0;
}