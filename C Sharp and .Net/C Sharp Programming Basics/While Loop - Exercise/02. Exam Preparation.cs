using System;
public class Program
	{
		public static void Main()
		{
			double cena = double.Parse(Console.ReadLine());
			double pari = double.Parse(Console.ReadLine());
			string transaction = "";
			double amount = 0;
			int day = 0;
			int harch = 0;
			string lasttrans = "";
		while (cena > pari)
		{
			day++;
			transaction = Console.ReadLine();
			amount = double.Parse(Console.ReadLine());

			if (transaction == "spend")
			{
				harch++;
				pari = Math.Max((pari - amount), 0.00);
			}
			else if (transaction == "save")
			{
				harch = 0;
				pari += amount;
			}

			if (harch==5)
            {
				break;
            }

		}

				
			if (harch == 5)
			{
				Console.WriteLine("You can't save the money.");
				Console.WriteLine(day);
			}
			else
			{
				Console.WriteLine("You saved the money for {0} days.", day);
			}
		}

	}

