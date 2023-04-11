using System;
					
public class Program
{
	public static void Main(){
		double budget=double.Parse(Console.ReadLine());
		int statisti=int.Parse(Console.ReadLine());
		double costperstatist=double.Parse(Console.ReadLine());
		double cost=0.0;
		if (statisti>150){
		cost=statisti*costperstatist*0.9+0.10*budget;
		}
		else {cost=statisti*costperstatist+0.10*budget;}
		
		if (cost>budget)
		{
		Console.WriteLine("Not enough money!");
		Console.WriteLine("Wingard needs {0:0.00} leva more.", cost-budget);
		}
		else
		{
			Console.WriteLine("Action!");
			Console.WriteLine("Wingard starts filming with {0:0.00} leva left.",budget-cost);
		}
	}	
}	