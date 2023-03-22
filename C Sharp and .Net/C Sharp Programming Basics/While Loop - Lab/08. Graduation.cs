using System;
					
public class Program
{
	public static void Main(){
	string kniga=Console.ReadLine();
	string check="";
	int counter=0;
		while(kniga != check & check !="No More Books")
		{
			
			check=Console.ReadLine();
			counter=counter+1;
			
		}
		if(check==kniga){
		Console.WriteLine("You checked {0} books and found it.", counter-1);
		}
		else
		{
		Console.WriteLine("The book you search is not here!");
		Console.WriteLine("You checked {0} books.", counter-1);

		}
	
	}

}