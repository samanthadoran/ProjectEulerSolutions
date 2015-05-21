#include <iostream>
bool isDiv(int num)
{
	for(int i = 11; i < 21; ++i)
	{
		if(num % i != 0)
		{
			return false;
		}
	}
	return true;
}


int main()
{
	int num = 1;

	while(!isDiv(num))
	{
		++num;
	}

	std::cout << num << std::endl;
}