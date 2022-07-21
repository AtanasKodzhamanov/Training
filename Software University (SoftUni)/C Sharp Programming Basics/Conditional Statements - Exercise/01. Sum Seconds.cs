using System;
					
public class Program
{
	public static void Main(){
		double a=double.Parse(Console.ReadLine());
		double bonus;
		if (a<101)
		{
			bonus=5;
		}
		else if (a>100 & a<1001)
		{
			bonus=a*0.2;
		}
		else {bonus=a*0.1;}
		if (a %2==0)
		{bonus=bonus+1;}
		if (a %10 == 5){bonus=bonus+2;}
		Console.WriteLine(bonus);
		Console.WriteLine(bonus+a);
	}	
}	