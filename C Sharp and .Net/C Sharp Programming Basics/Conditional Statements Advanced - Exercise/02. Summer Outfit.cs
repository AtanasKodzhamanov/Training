using System;
					
public class Program
{
	public static void Main(){
	
		string type=Console.ReadLine();
		int broi=int.Parse(Console.ReadLine());
		int budget=int.Parse(Console.ReadLine());
		
		double pr=5;
		double pd=3.8;
		double pt=2.8;
		double pn=3;
		double pg=2.5;
		double cost=0;
	
		switch(type)
		{
			case "Roses":
				if(broi>80)
				{
					cost=broi*pr*0.9;
				}
				else{cost=broi*pr;}	
			break;
			case "Dahlias":
				if(broi>90)
				{
					cost=broi*pd*0.85;
				}
				else{cost=broi*pd;}	
			break;
			case "Tulips":
				if(broi>80)
				{
					cost=broi*pt*0.85;
				}
				else{cost=broi*pt;}	
			break;
			case "Narcissus":
				if(120>broi)
				{
					cost=broi*pn*1.15;
				}
				else{cost=broi*pn;}	
			break;
			case "Gladiolus":
				if(80>broi)
				{
					cost=broi*pg*1.2;
				}
				else{cost=broi*pg;}	
			break;
		}
		
		if (budget-cost >=0){	
		Console.WriteLine("Hey, you have a great garden with {0} {1} and {2:0.00} leva left.", broi, type, budget-cost);
		}
		else 
		{Console.WriteLine("Not enough money, you need {0:0.00} leva more.",cost-budget);}
	}
	
}		