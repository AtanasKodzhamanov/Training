using System;
					
public class Program
{
	public static void Main(){
		string den=Console.ReadLine();
		string status="";
		
		switch(den)
		{
				case "banana":
				case "apple":
				case "kiwi":
				case "cherry":
				case "lemon":
				case "grapes":
				status="fruit";
				break;
				case "tomato":
				case "cucumber":
				case "pepper":
				case "carrot":
				status="vegetable";
				break;
			default:
				status="unknown";
				break;
				
			
		}
	Console.WriteLine(status);
	}
	
}	