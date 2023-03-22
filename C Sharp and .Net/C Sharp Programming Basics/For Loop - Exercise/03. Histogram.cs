using System;
					
public class Program
{
	public static void Main(){
	
	int n = int.Parse(Console.ReadLine());
	double zaplata=double.Parse(Console.ReadLine());
	string website="";
		for(int i=1; i<=n; i++)
		{
			website = Console.ReadLine();
			if(website=="Facebook")
			{
				zaplata=zaplata-150;
			}
			else if(website=="Instagram")
			{
				zaplata=zaplata-100;
			}
			else if(website=="Reddit")
			{
							zaplata=zaplata-50;

			}
		
		}
		if (zaplata<=0)
		{Console.WriteLine("You have lost your salary.");
		}
		else{
		Console.WriteLine(zaplata);
		}

		
	}

}	