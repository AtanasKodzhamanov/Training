	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		double n1 = double.Parse(Console.ReadLine());
		double n2 = double.Parse(Console.ReadLine());
		string op= Console.ReadLine();
		string re = "";
	
		if (op== "+")
		{
			if ((n1 + n2) % 2 == 0)
			{
				 re = "even";
			}
			else re = "odd";

			Console.WriteLine("{0} {1} {2} = {3} - {4}", n1,op , n2, n1 + n2, re);
        }
		else if (op== "-")
		{
			if ((n1 - n2) % 2 == 0)
			{
				 re = "even";
			}
			else re = "odd";

			Console.WriteLine("{0} {1} {2} = {3} - {4}", n1,op , n2, n1 - n2, re);
		}
		else if (op== "*")
		{
			if ((n1 * n2) % 2 == 0)
			{
				 re = "even";
			}
			else re = "odd";

			Console.WriteLine("{0} {1} {2} = {3} - {4}", n1,op ,n2, n1 * n2, re);
		}
		else if (op== "/")
		{
			if(n2==0)
            {
				Console.WriteLine("Cannot divide {0} by zero", n1);
            }
            else
            {
				Console.WriteLine("{0} {1} {2} = {3:0.00}", n1,op , n2, n1 / n2);
			}
		}
		else if (op== "%")
		{
			if (n2 == 0)
			{
				Console.WriteLine("Cannot divide {0} by zero", n1);
			}
			else
			{
				Console.WriteLine("{0} {1} {2} = {3}", n1, op, n2, n1 % n2);
			}
		}



	}
}




