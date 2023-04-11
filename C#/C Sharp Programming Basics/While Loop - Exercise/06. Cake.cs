	using System;
using System.Data;

public class Program
	{
	public static void Main()
	{

		for (int i = 0; i <= 23; i++)
		{
			for (int j = 0; j <60; j++)
			{
				if (j == 60)
                {
					Console.WriteLine("{0}:{1}", i, 00);
				}
				else {
					Console.WriteLine("{0}:{1}", i, j); }
			}
		}

	}
}