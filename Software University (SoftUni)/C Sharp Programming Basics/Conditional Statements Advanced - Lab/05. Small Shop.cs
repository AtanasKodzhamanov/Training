using System;
					
public class Program
{
	public static void Main(){

		double kolichestvo=double.Parse(Console.ReadLine());
		
		if (kolichestvo>=-100 & kolichestvo<=100)
		{ 
			if(kolichestvo==0)
			{
		Console.WriteLine("No");
			}
		 	else{	Console.WriteLine("Yes");}
		}
		else{Console.WriteLine("No");}
	
	}
	
}	