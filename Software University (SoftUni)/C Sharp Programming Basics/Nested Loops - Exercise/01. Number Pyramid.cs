	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
{
	public static void Main()
	{
		int first = int.Parse(Console.ReadLine());
		int second = int.Parse(Console.ReadLine());
		string currnums = "";
		int currnum = 0;

		for (int i = first; i <= second; i++) 
        {
			currnums = i.ToString();
			int odd = 0;
			int even = 0;
			
			for (int j = 0; j < currnums.Length; j++)
			{
				if (j %2== 0)
				{
					currnum=int.Parse(currnums[j].ToString());
					even += currnum;
				}
				else
                {
					currnum = int.Parse(currnums[j].ToString());
					odd += currnum;
				}
                
            }
            if(odd==even)
			{
				Console.Write(i +" ") ;
            }				
        }
	
	}
}


