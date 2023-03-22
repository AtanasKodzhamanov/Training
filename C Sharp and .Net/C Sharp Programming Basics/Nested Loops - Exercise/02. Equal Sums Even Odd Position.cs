	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
	
		string input = "";
		int number = 0;
		int a = 0;
		int prime = 0;
		int nonprime = 0;
		while(true)
		{
			input = Console.ReadLine();
			bool r = int.TryParse(input, out number);
			if (input == "stop")
            {
				break;
            }
			if (number < 0)
			{
				Console.WriteLine("Number is negative.");
			}
			else
			{
				for (int j = 1; j <= number; j++)
				{
					if (number % j == 0)
					{
						a++;
					}


				}
				if (a == 2)

                {
					prime += number;
                }
				else { nonprime += number; }
				a = 0;
			}
		}
		Console.WriteLine("Sum of all prime numbers is: " + prime);
		Console.WriteLine("Sum of all non prime numbers is: " + nonprime);
		
	}
}

