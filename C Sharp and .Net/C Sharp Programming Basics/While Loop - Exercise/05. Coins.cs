	using System;
using System.Data;

public class Program
	{
	public static void Main()
	{
		int width = int.Parse(Console.ReadLine());
		int length = int.Parse(Console.ReadLine());
		int cake = width * length;
		int taken = 0;
		string command = "";
		while (cake >= 0)
		{
			command=Console.ReadLine();
			if(command=="STOP")
			{ Console.WriteLine("{0} pieces are left.", Math.Abs(cake));break;}
			bool r = int.TryParse(command, out taken);
			cake = cake - taken;

			if(cake<0)
            {
				Console.WriteLine("No more cake left! You need {0} pieces more.", Math.Abs(cake));
            }
			
		}
		
		

	}
}