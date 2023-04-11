using System;
					
public class Program
{
	public static void Main(){
	
	int n = int.Parse(Console.ReadLine());
	int chislo=0;
	double p1=0;
	double p2=0;
	double p3=0;
	double p4=0;
	double p5=0;
		for(int i=1; i<=n; i++)
		{
			chislo = int.Parse(Console.ReadLine());
			if(chislo<200)
			{
				p1=p1+1;
			}
			else if(chislo>=200 & chislo<400)
			{
				p2=p2+1;
			}
			else if(chislo>=400 & chislo<600)
			{
				p3=p3+1;
			}
			else if(chislo>=600 & chislo<800)
			{
				p4=p4+1;
			}
			else if(chislo>=800 )
			{
				p5=p5+1;
			}
		}
		Console.WriteLine("{0:0.00}%",(p1/n*100));
		Console.WriteLine("{0:0.00}%",(p2/n*100));
		Console.WriteLine("{0:0.00}%",(p3/n*100));
		Console.WriteLine("{0:0.00}%",(p4/n*100));
		Console.WriteLine("{0:0.00}%",(p5/n*100));
		
	}

}
		