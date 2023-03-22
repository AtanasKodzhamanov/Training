using System;
					
public class Program
{
	public static void Main(){
		int broi=int.Parse(Console.ReadLine());
		string zadacha="";
		int broitot=broi;
		int ocenka=0;
		double gp=0;
		double counter=0;
		string last="";
		while(zadacha != "Enough" & broi>0)
		{last=zadacha;
			zadacha=Console.ReadLine();
			if (zadacha != "Enough")
			{
			ocenka=int.Parse(Console.ReadLine());
			if (ocenka<=4){
			broi=broi-1;
			}
			gp=gp+ocenka;
			counter=counter+1;
			}
		}
		
		if(zadacha=="Enough")
		{
			Console.WriteLine("Average score: {0:0.00}", gp/counter);
			Console.WriteLine("Number of problems: "+counter);
			Console.WriteLine("Last problem: "+ last);
		}
		else
		{
			Console.WriteLine("You need a break, {0} poor grades.", broitot); 
		}
	}

}