	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		int chislo = int.Parse(Console.ReadLine());
		int razbito = 0;
		int a =0;
		for (int i = 1111; i <= 9999; i++)
		{
			string currentnum = i.ToString();
			a = 0;
			for (int j = 0; j < 4; j++)
			{
				razbito = int.Parse(currentnum[j].ToString()) ;
				if (razbito != 0)
				{
					if (chislo % razbito == 0)
					{ a++; }
					if (a == 4)
					{
						Console.Write(i + " ");
					}
				}
			}


        }		
    }
}

