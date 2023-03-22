	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		double budget = double.Parse(Console.ReadLine());
		string season = Console.ReadLine();
		string dest = "";
		string accom = "";
		double spend = 0;
		if(budget<=100)
        {
			dest = "Bulgaria";
			if (season == "winter")
			{
				spend = budget * 0.7;
				accom = "Hotel";
			}
			else { spend = budget * 0.3; accom = "Camp"; }
        }
		 else if (budget <= 1000 & budget>100)
		{
			dest = "Balkans";
			if (season == "winter")
			{
				spend = budget * 0.8;
				accom = "Hotel";
			}
			else { spend = budget * 0.4; accom = "Camp"; }
		}
		if (budget > 1000)
		{
			dest = "Europe";
			accom = "Hotel";
			spend = budget * 0.9;
		}

		Console.WriteLine("Somewhere in {0}", dest);
		Console.WriteLine("{0} - {1:0.00}", accom,spend);
	
    }
}
