	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{

		int juri = int.Parse(Console.ReadLine());
		double ocenka = 0;
		double avg = 0;
		double presentacii = 0;
		double total = 0;
		double final = 0;
        while(true)
		{
		string title = Console.ReadLine();
		if (title == "Finish") { Console.WriteLine("Student's final assessment is {0:0.00}.", (total / presentacii));  break; }
			
			
			for(int i=1;i<=juri;i++)
            {
				ocenka = double.Parse(Console.ReadLine());
				avg += ocenka;
            }
			Console.WriteLine("{0} - {1:0.00}.", title, avg / juri);
			presentacii++;
			total = total + avg/juri;
			avg = 0;
			final = total / presentacii;
			//Console.WriteLine("HERE:"+ final +"Pres: "+ presentacii);
		}		
	}
}



