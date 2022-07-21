using System;
					
public class Program
{
	public static void Main(){
	
		
	int n=int.Parse(Console.ReadLine());
	int chislo=0;
	int min=0;
	int max=0;
		for (int i=0; i<n; i++)
	{			chislo=int.Parse(Console.ReadLine());

		if (i==0)
		{
			min=chislo;
			max=chislo;
		}
		if (chislo>max)
		{max=chislo;}
		if (chislo<min)
		{min=chislo;}
	}
		Console.WriteLine("Max number: "+max);
		Console.WriteLine("Min number: "+min);
	}
	
}	