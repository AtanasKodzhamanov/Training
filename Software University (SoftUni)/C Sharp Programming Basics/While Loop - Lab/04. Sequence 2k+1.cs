using System;
					
public class Program
{
	public static void Main(){
	string input="";
	double number=0;
	bool result = true;
	double total=0;
	while(result==true)
	{	
	
		input=Console.ReadLine();
		result = double.TryParse(input, out number);
		if(result == true){	
		
		if (number<0)
		{
			Console.WriteLine("Invalid operation!");
			result=false;
		}
		else {Console.WriteLine("Increase: {0:0.00}",number);
		total=total+number;}
		}
	}
	Console.WriteLine("Total: {0:0.00}",total);
		
	}

}
	