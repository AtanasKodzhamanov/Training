using System;
					
public class Program
{
	public static void Main(){
	string input="";
	int number=int.MinValue;
	bool result = true;
	double total=0;
	int max=int.MaxValue;
	while(result==true)
	{	
		input=Console.ReadLine();
		result = int.TryParse(input, out number);
		if (result==true)
		{
			if(max>number)
		{max=number;}}
		//Console.WriteLine(max + " " + number);
	}
		Console.WriteLine(max);
	}

}