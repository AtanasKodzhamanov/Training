using System;
					
public class Program
{
	public static void Main(){
		string figure=Console.ReadLine();

		if (figure =="square") {
		double a=double.Parse(Console.ReadLine());
		double	area=a*a;
			Console.WriteLine(area);
		}
		else if(figure=="rectangle"){
		double a=double.Parse(Console.ReadLine());
					double b=double.Parse(Console.ReadLine());

		double	area=a*b;
			Console.WriteLine(area);
		}
	else if(figure=="circle"){
		double a=double.Parse(Console.ReadLine());

		double	area=a*a*Math.PI;
			Console.WriteLine(area);
		}
		else if(figure=="triangle"){
		double a=double.Parse(Console.ReadLine());
		double b=double.Parse(Console.ReadLine());

		double	area=a*b/2;
			Console.WriteLine(area);
		}
	
	}	
}	