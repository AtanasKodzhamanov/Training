using System;
					
public class Program
{
	public static void Main(){
	
		
		int r=int.Parse(Console.ReadLine());
		string time=Console.ReadLine();
		string outfit="";
		string shoes="";

		if (r>=10 & r<=18)
		{
			if(time=="Morning")
			{
				outfit="Sweatshirt";
				shoes="Sneakers";
			}
			else if(time=="Afternoon")
			{	
				outfit="Shirt";
				shoes="Moccasins";
			}
			else if(time=="Evening")
			{
				outfit="Shirt";
				shoes="Moccasins";
			}
		}
		else if (r>18 & r<=24)
		{
			if(time=="Morning")
			{
			outfit="Shirt";
				shoes="Moccasins";
			}
			else if(time=="Afternoon")
			{	
				outfit="T-Shirt";
				shoes="Sandals";
			}
			else if(time=="Evening")
			{
outfit="Shirt";
				shoes="Moccasins";
			}
		}
		else if (r>=25)
		{
		if(time=="Morning")
			{
				outfit="T-Shirt";
				shoes="Sandals";
			}
			else if(time=="Afternoon")
			{	
				outfit="Swim Suit";
				shoes="Barefoot";
			}
			else if(time=="Evening")
			{
				outfit="Shirt";
				shoes="Moccasins";
			}
		}
		
		Console.WriteLine("It's {0} degrees, get your {1} and {2}.",r,outfit,shoes);
	}
	
}	