using System;
					
public class Program
{
	public static void Main(){
	
	int n = int.Parse(Console.ReadLine());
	int max=int.MinValue;	
	int chislo=0;
	int sum=0;
		for(int i=1; i<=n; i++)
		{
			chislo = int.Parse(Console.ReadLine());
			if (chislo>max)
			{
				max=chislo;
			}
			sum=sum+chislo;
		}
	if(sum-max==max)
	{
		Console.WriteLine("Yes");
		Console.WriteLine("Sum = " +max);
	}
	else{
	Console.WriteLine("No");
	Console.WriteLine("Diff = "+Math.Abs(max-(sum-max)));
		
	}

}
		
}	