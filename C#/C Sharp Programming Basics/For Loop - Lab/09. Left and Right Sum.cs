using System;
					
public class Program
{
	public static void Main(){
	
		
	int n=int.Parse(Console.ReadLine());
	int chislo=0;
	int oddtot=0;
	int eventot=0;
		for (int i=1; i<=n; i++)
	{	
		chislo=int.Parse(Console.ReadLine());
		
			if(i%2 ==0)
			{
			eventot=eventot+chislo;	
			}
			else{oddtot=oddtot+chislo;}
		
	}
		if(eventot==oddtot){
		Console.WriteLine("Yes");
		Console.WriteLine("Sum = "+eventot);}
		else {
		Console.WriteLine("No");
		Console.WriteLine("Diff = "+Math.Abs(eventot-oddtot));
		}
		}
		
	}