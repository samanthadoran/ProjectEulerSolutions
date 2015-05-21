class Fibonacci
{

	int sumEven(int x, int y)
	{
		int sum = 0;

		while(x < 4000000 && y < 4000000)
		{
			if(x % 2 == 0)
			{
				sum+=x;
			}
			if(y % 2 == 0)
			{
				sum+=y;
			}

			/*Note: we do these assignments twice to ensure we do not add the
			 *same number to the sum more than once*/
			int temp = y;

			y = x + y;
			x = temp;

			temp = y;

			y = x + y;
			x = temp;
		}

		return sum;
	}

	public static void main(String[] args)
	{
		Fibonacci fib = new Fibonacci();
		int sum = fib.sumEven(1,2);

		System.out.println(sum);
	}
}