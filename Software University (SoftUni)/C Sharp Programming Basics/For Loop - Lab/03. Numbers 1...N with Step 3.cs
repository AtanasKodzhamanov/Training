using System;
					
public class Program
{
	public static void Main(){
	
		
	int n=int.Parse(Console.ReadLine());
	int power=2;
	for (int i=1; n>=i; i++)
	{	power=power*2;
		if (i==1)
		{
				Console.WriteLine(1);
			power=2;
		}
		else if (i%2==0){
		
		Console.WriteLine(power);
		
		}
	}
	}
	
}	