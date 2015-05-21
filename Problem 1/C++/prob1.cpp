#include <iostream>

int main()
{
	long long int sum = 0;

	int k = 1000;

	for(int i = 1; i < k; ++i)
	{
		if(i % 3 == 0 || i % 5 == 0)
		{
			sum+=i;
		}
	}

	std::cout << sum << std::endl;
}