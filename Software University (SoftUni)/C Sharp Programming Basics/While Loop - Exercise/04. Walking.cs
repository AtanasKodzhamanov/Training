	using System;
	public class Program
	{
	public static void Main()
	{

		double coins = double.Parse(Console.ReadLine());
		coins = coins * 100;
		int numcoin = 0;
		int pause = 0;
		while (coins >= 0 )
		{
			pause = 0;
			if (coins - 2 * 100 >= 0)
			{
				coins=coins- 2 * 100;
				numcoin++;
				pause = 1;
			}
			else if (coins-1 * 100 >= 0 & pause == 0)
            {
				coins = coins - 1 * 100;
				numcoin++;
				pause = 1;
			}
			else if(coins-0.50 * 100 >= 0 & pause ==0)
            {
				coins = coins - 0.5 * 100;
				numcoin++;
				pause = 1;
			}
			else if (coins - 0.20 * 100 >= 0 & pause == 0)
			{
				coins = coins - 0.2 * 100;
				numcoin++;
				pause = 1;
			}
			else if (coins - 0.10 * 100 >= 0 & pause == 0)
			{
				coins = coins - 0.1 * 100;
				numcoin++;
				pause = 1;
			}
			else if (coins - 0.05 * 100 >= 0 & pause == 0)
			{
				coins = coins - 0.05 * 100;
				numcoin++;
				pause = 1;
			}
			else if (coins - 0.02 * 100 >= 0 & pause == 0)
			{
				coins= coins- 0.02 * 100;
				numcoin++;
				pause = 1;


				//Console.WriteLine(coins);
				//Console.WriteLine(numcoin);
				//Console.WriteLine("---");
			}
			else if (coins - 0.01 * 100 >= 0 & pause == 0)
			{
				coins=coins- 0.01 * 100;
				numcoin++; 
				pause = 1;

				//Console.WriteLine(coins);
				//Console.WriteLine(numcoin);
				//Console.WriteLine("---");
			}
            else { break; }
		}
		Console.WriteLine(numcoin);

	}
}
