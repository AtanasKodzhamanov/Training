using System;
					
public class Program
{
	public static void Main(){
		string product=Console.ReadLine();
		string grad=Console.ReadLine();
		double kolichestvo=double.Parse(Console.ReadLine());
		double cost=0.0;
				double pcof=0.5;
				double pwat=0.8;
				double pbeer=1.2;
				double psweets=1.45;
				double ppeanuts=1.60;
			switch(grad)
		{
			case "Sofia":
				pcof=0.5;
				pwat=0.8;
				pbeer=1.2;
				psweets=1.45;
				ppeanuts=1.60;
				break;
			case "Plovdiv":
			pcof=0.4;
				pwat=0.7;
				pbeer=1.15;
				psweets=1.3;
				ppeanuts=1.5;
				break;
			case "Varna":
			pcof=0.45;
				pwat=0.7;
				pbeer=1.10;
				psweets=1.35;
				ppeanuts=1.55;
				break;
			default:
				Console.WriteLine("unknown");
				break;
		}	
		
		switch(product)
		{
			case "coffee":
				cost=kolichestvo*pcof;
			break;
			case "water":
								cost=kolichestvo*pwat;

			break;
			case "beer":
								cost=kolichestvo*pbeer;

			break;
			case "sweets":
								cost=kolichestvo*psweets;

			break;
			case "peanuts":
								cost=kolichestvo*ppeanuts;

			break;
		}
		
		
	
				Console.WriteLine(cost);
	}
	
}	