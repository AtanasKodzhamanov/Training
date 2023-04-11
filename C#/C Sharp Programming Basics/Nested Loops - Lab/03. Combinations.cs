	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
	{
	public static void Main()
	{
		int start = int.Parse(Console.ReadLine());
		int end = int.Parse(Console.ReadLine());
		int magic = int.Parse(Console.ReadLine());
		int count = 0;
		int endd = 0;
		for (int i = start; i <= end; i++)
		{
			for (int j = start; j <= end; j++)
			{
				count++;
                if (j + i == magic) {  Console.WriteLine("Combination N:{0} ({1} + {2} = {3})", count, i, j, magic);endd = 1; break; }
               
				//Console.WriteLine(count);
				//Console.WriteLine("i= "+i);
				//Console.WriteLine("j= "+j);
			

			}
			if (endd==1)
			{ break; }
            
		}
		if (endd == 0)
		{
			Console.WriteLine("{0} combinations - neither equals {1}",count,magic);
		}
		else
		{
			//Console.WriteLine("Combination N:{0} ({1}+{2}={3})",count,i,j,magic);
		}
	}
}
