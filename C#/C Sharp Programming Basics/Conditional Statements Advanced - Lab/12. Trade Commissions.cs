using System;
					
public class Program
{
	public static void Main(){
	
		string type=Console.ReadLine();
		int r=int.Parse(Console.ReadLine());
		int c=int.Parse(Console.ReadLine());
		double total=0;
		
		if (type=="Premiere")
		{total=r*c*12;}
		else if(type=="Normal")
		{total=r*c*7.5;}
		else if(type=="Discount")
		{total=r*c*5;}
		Console.WriteLine("{0:0.00} leva",total);
	}
	
}	