using System;
					
public class Program
{
	public static void Main(){
	
		
	int n=int.Parse(Console.ReadLine());
	int chislo=0;
	int totalone=0;
	int totaltwo=0;
		for (int i=1; i<=n*2; i++)
	{	
		chislo=int.Parse(Console.ReadLine());

		if (i<=n)
		{
			totalone=totalone+chislo;
		}
			 else if (i>n)
			 {totaltwo=totaltwo+chislo;}
			
	}
		if(totalone==totaltwo)
		{
			Console.WriteLine("Yes, sum = "+totalone);
		}
		else{
		int diff=totalone-totaltwo;
		Console.WriteLine("No, diff = "+Math.Abs(diff));	
		}
	}
	
}	