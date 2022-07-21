using System;
					
public class Program
{
	public static void Main(){
		int a=int.Parse(Console.ReadLine());
		int b=int.Parse(Console.ReadLine());
		int c=int.Parse(Console.ReadLine());
		int sum=a+b+c;
		int minutes=sum/60;
		int secondss=sum % 60;
		if (secondss<10)
		{
			Console.WriteLine($"{minutes}:0{secondss}");
		}
		else 
		{
		Console.WriteLine($"{minutes}:{secondss}");
		}
		
	}	
}	
