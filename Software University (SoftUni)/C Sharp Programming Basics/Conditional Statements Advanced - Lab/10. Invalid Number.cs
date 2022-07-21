using System;
					
public class Program
{
	public static void Main(){
		string plod=Console.ReadLine();
		string den=Console.ReadLine();
		double kg=double.Parse(Console.ReadLine());
		int error=0;
	double		pb=0;
	double			pa=0;
	double			po=0;
	double			pg=0;
	double			pk=0;
	double			pp=0;
	double		pgr=0;
double cost=0;
	switch(den)
	{
		case "Monday":
		case "Tuesday":
		case "Wednesday":
		case "Thursday":
		case "Friday":
			pb=2.50;
			pa=1.2;
			po=0.85;
			pg=1.45;
			pk=2.7;
			pp=5.5;
			pgr=3.85;
			break;
		case "Saturday":
		case "Sunday":
			pb=2.70;
			pa=1.25;
			po=0.9;
			pg=1.6;
			pk=3;
			pp=5.6;
			pgr=4.2;
			break;
		default:
			error=1;
			break;
	}
	
		
		if(plod=="banana"){
	cost=kg*pb;	
		}
		else if (plod=="apple"){
			cost=kg*pa;	
		}
		else if (plod=="orange"){
			cost=kg*po;	
		}
		else if (plod=="grapefruit"){
			cost=kg*pg;	
		}
		else if (plod=="kiwi"){
			cost=kg*pk;	
		}
		else if (plod=="pineapple"){
			cost=kg*pp;	
		}
		else if (plod=="grapes"){
			cost=kg*pgr;	
		}
		else {error=1;}
		
		if (error==1)
		{
		Console.WriteLine("error");
		}
		else {	Console.WriteLine("{0:0.00}",cost);};
	
	}
	
}	