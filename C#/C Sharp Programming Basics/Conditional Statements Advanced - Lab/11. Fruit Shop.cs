using System;
					
public class Program
{
	public static void Main(){
		string grad=Console.ReadLine();
		double s=double.Parse(Console.ReadLine());
		int error=0;
		double pa=0;
		double pb=0;
		double pc=0;
		double pd=0;
		double komisionna=0;
		switch(grad){
			case "Sofia":
				pa=5;
				pb=7;
				pc=8;
				pd=12;
			break;
			case "Varna":
					pa=4.5;
				pb=7.5;
				pc=10;
				pd=13;
			break;	
			case "Plovdiv":
					pa=5.5;
				pb=8;
				pc=12;
				pd=14.5;
			break;	
			default:
				error=1;
			break;
		}
		
		if (s>=0 & s<=500)
		{
			komisionna=pa*s/100;
		}
		else if (500<s & s<=1000)
		{komisionna=pb*s/100;
		}
		else if (1000<s & s<=10000)
		{komisionna=pc*s/100;
		}
		else if (s>10000)
		{komisionna=pd*s/100;
		}
		else {error=1;}
		
		if(error==1)
		{
			Console.WriteLine("error");
		}
		else {Console.WriteLine("{0:0.00}",komisionna);}
		
	}
	
}	