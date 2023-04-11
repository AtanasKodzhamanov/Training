using System;
					
public class Program
{
	public static void Main(){
		double record=double.Parse(Console.ReadLine());
		double distance=double.Parse(Console.ReadLine());
		double speed=double.Parse(Console.ReadLine());
	
		double delaytimes=Math.Floor(distance/15);
		double totaldelay=delaytimes*12.5;
		double vanchotime=distance*speed+totaldelay;
		
		if(record>vanchotime)
		{
			Console.WriteLine("Yes, he succeeded! The new world record is {0:0.00} seconds.", vanchotime);
		}
		else
		{
					Console.WriteLine("No, he failed! He was {0:0.00} seconds slower.", vanchotime-record);
		}
		
	}	
}		