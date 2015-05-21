#include <iostream>
#include <math.h>

bool isPrime(int k)
{
	int factors = 0;
	for(int i = 1; i < sqrt(k)+1; ++i)
	{
		if(k%i == 0)
		{
			++factors;
		}

		if(factors >= 2)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int factor = 3;
	int pFactor = 0;
	unsigned long long int number = 600851475143;

	while(factor < sqrt(number)+1)
	{
		if(number % factor == 0 && factor % 2 != 0)
		{
			if(isPrime(factor))
			{
				pFactor = factor;
			}
		}

		factor+=2;
	}
	std::cout <<pFactor << std::endl;

	return 0;
}