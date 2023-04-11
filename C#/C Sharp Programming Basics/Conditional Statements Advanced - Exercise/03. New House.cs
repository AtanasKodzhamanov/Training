	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		double budget = int.Parse(Console.ReadLine());
		string season = Console.ReadLine();
		int ribari = int.Parse(Console.ReadLine());
		double naem = 0;
        switch (season)
        {
			case "Spring":
				naem = 3000;
				break;
			case "Summer":
			case "Autumn":
				naem = 4200;
				break;
			case "Winter":
				naem = 2600;
				break;
        }

		if(ribari<=6)
        {
			naem = naem * 0.9;
        }
		else if(ribari>=7 & ribari<=11)
        {
			naem = naem * 0.85;
        }
		else if (ribari >= 12)
		{
			naem = naem * 0.75;
		}

		if(season !="Autumn" & ribari %2==0)
        {
			naem = naem * 0.95;
        }

		if (budget >= naem)
		{
			Console.WriteLine("Yes! You have {0:0.00} leva left.", budget - naem);
		}
		else Console.WriteLine("Not enough money! You need {0:0.00} leva.",naem-budget);

        	
    }
}
		