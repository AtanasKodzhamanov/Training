	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		double hi = double.Parse(Console.ReadLine());
		double mi = double.Parse(Console.ReadLine());
		double h = double.Parse(Console.ReadLine());
		double m = double.Parse(Console.ReadLine());

		double timeizpit = hi * 60 + mi;
		double timearrival = h * 60 + m;
		double delay=timearrival-timeizpit;

		if (delay > 0)
		{
			Console.WriteLine("Late");
		}
		else if (delay <= 0 & delay >= -30)
		{
			Console.WriteLine("On time");
			}
		else Console.WriteLine("Early");

		if(delay>=-59 & delay<0)
        {
			Console.WriteLine("{0} minutes before the start.", Math.Abs(delay));
        }
		else if(delay<=-60)
        {
			Console.WriteLine("{0} {1:00} hours before the start.", Math.Floor(Math.Abs(delay)/60), Math.Abs(delay)%60);
		}
		else if(delay<60 & delay>0)
        {
			Console.WriteLine("{0} minutes after the start.", delay);
		}
		else Console.WriteLine("{0} {1:00} hours after the start.", Math.Floor(delay / 60), delay % 60);
	}
}



