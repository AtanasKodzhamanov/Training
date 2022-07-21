using System;
					
public class Program
{
	public static void Main(){
	
		
	int n=int.Parse(Console.ReadLine());
	int chislo=0;

		int total=0;
		for (int i=0; i<n; i++)
	{	
		chislo=int.Parse(Console.ReadLine());
		total=total+chislo;
	}
		Console.WriteLine(total);
		
	}
	
}	