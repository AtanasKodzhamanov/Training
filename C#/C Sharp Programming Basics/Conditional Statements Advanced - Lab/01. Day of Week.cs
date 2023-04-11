using System;
					
public class Program
{
	public static void Main(){
		string dohod=Console.ReadLine();
			
		switch(dohod)
		{
			case "Monday":
			case "Tuesday":
			case "Wednesday":
			case "Thursday":
			case "Friday":
				Console.WriteLine("Working day");
				break;
			case "Saturday":
			case "Sunday":
				Console.WriteLine("Weekend");
				break;
			default:
				Console.WriteLine("Error");
				break;
		}
	}
	
}	