using System;
					
public class Program
{
	public static void Main(){
		int hour=int.Parse(Console.ReadLine());
		int min=int.Parse(Console.ReadLine());
		
		if (min>=45)
		{
			if (hour<23){
			hour=hour+1;}
			else {hour=0;}
			min=min+15-60;
		}
		else {min=min+15;}
		if (min==60){min=0;}
		Console.WriteLine("{0:0}:{1:00}",hour,min);
	}	
}	