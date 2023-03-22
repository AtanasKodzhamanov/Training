	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
	{
	public static void Main()
	{
		string input = "";
		double cena = 0;
		double savings = 0;
		double dohod = 0;
		while(input != "End")
        {
			input = Console.ReadLine();
            if (input == "End") { break; }
			cena = double.Parse(Console.ReadLine());
			while(cena>savings)
            {
				dohod = double.Parse(Console.ReadLine());
				savings += dohod;
            }
			Console.WriteLine("Going to {0}!", input);
			savings = 0;

        }
		return;
	}
}