	using System;
	public class Program
	{
		public static void Main()
		{
			int steps = 0;
			string command = "";
			int total = 0;
			bool result;
			while(total<=10000)
			{
				command = Console.ReadLine();
				result = int.TryParse(command, out steps);
				total += steps;

				if(command=="Going home")
				{
					command = Console.ReadLine();
					result = int.TryParse(command, out steps);
					total += steps;
					break;
				}
			}

			if (total>=10000)
			{
			Console.WriteLine("Goal reached! Good job!");
			Console.WriteLine("{0} steps over the goal!", total - 10000);
			}
			else
			{
				Console.WriteLine("{0} more steps to reach goal.", 10000 - total);
			}
		}
	}
