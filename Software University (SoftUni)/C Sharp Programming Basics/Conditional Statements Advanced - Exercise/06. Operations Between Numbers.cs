	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		string mesec= Console.ReadLine();
		double nights = double.Parse(Console.ReadLine());
		double studio = 0;
		double flat = 0;
		switch(mesec)
        {
			case "May":
			case "October":
				studio = 50;
				flat = 65;
				if (nights>7 & nights<=14)
                {
					studio = 50 * 0.95;
                }
				else if(nights>14)
                {
					studio = 50 * 0.7;
					flat = flat * 0.9;
                }
				break;
			case "June":
			case "September":
				studio = 75.2;
				flat = 68.7;
				if (nights > 14)
				{
					studio = studio * 0.8;
					flat = flat * 0.9;
				}
			
				break;
			case "July":
			case "August":
				studio = 76;
				flat = 77;
				if (nights > 14)
				{
			
					flat = flat * 0.9;
				}
				break;


        }

		Console.WriteLine("Apartment: {0:0.00} lv.", flat * nights);
		Console.WriteLine("Studio: {0:0.00} lv.", studio * nights);


	}
}