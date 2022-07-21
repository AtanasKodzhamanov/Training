	using System;
using System.Data;

public class Program
	{
	public static void Main()
	{
		int total = 0;
		int number = int.Parse(Console.ReadLine());

		for (int i = 0; i <= number; i++)
		{
			for (int j = 0; j <= number; j++)
			{
				for (int k = 0; k <= number; k++)
				{
					if(j+k+i==number)
                    {
						total++;
                    }

				}

			}
		}
		Console.WriteLine(total);

	}
}
