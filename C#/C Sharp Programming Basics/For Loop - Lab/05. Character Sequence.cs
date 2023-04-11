using System;
					
public class Program
{
	public static void Main(){
	
		
	//int n=int.Parse(Console.ReadLine());
	string input=Console.ReadLine();
	int total=0;
		for (int i=0; i<input.Length; i++)
	{	
			char letter=input[i];
			string a=letter.ToString();
			switch(a)
			{
				case "a":
				total=total+1;
				break;
				case "e":
				total=total+2;
				break;
				case "i":
				total=total+3;
				break;
				case "o":
				total=total+4;
				break;
				case "u":
				total=total+5;
				break;
			}
	}
		Console.WriteLine(total);
		
	}
	
}