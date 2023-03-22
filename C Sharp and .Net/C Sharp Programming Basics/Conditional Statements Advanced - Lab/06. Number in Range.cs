using System;
					
public class Program
{
	public static void Main(){
		int chas=int.Parse(Console.ReadLine());
		string den=Console.ReadLine();
		string status="";
		
		switch(den)
		{
			case "Monday":
			case "Tuesday":
			case "Wednesday":
			case "Thursday":
			case "Friday":
			case "Saturday":
				if(chas>=10 &chas<=18)
				{status="open";}
				else {status="closed";}
			break;
			case "Sunday":
				status="closed";
			break;
		}
	Console.WriteLine(status);
	}
	
}	