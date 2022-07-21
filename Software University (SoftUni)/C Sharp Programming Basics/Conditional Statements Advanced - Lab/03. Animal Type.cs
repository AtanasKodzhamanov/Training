using System;
					
public class Program
{
	public static void Main(){
		double age=double.Parse(Console.ReadLine());
		string dohod=Console.ReadLine();
			string title="";
		switch(dohod)
		{
			case "f":
				if (age>=16)			
				{
					title="Ms.";
				}
				else {title="Miss";}
				break;
			case "m":
			if (age>=16)			
				{
					title="Mr.";
				}
				else {title="Master";}
				break;

			default:
				Console.WriteLine("unknown");
				break;
		}	
				Console.WriteLine(title);
	}
	
}	