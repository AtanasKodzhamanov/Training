	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		int chislo = int.Parse(Console.ReadLine());
		int left = chislo;
		int num = 1;
		int printnum = 0;
		string print = "";
		while(true)
		{

			for (int i = 0; i < num; i++)
			{ chislo--;
				printnum++;
				if (chislo >= 0)
				{
					if (i == 0)
					{
						print = printnum.ToString();

					}
					else
					{
						print = print + " " + printnum.ToString();
					}
				}
			}
			Console.WriteLine(print);
			num++;
			print = "";
			if (chislo <= 0) { break; }
		}


	}
}   