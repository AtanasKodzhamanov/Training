using System;
					
public class Program
{
	public static void Main(){
	
	string name=Console.ReadLine();
	double grade=0;
	double old=0;
	int fail=0;
	int klas=0;
	double gpa=0;
	double total=0;
	string stop="false";
		while(klas<=13 & stop=="false")
	{	klas=klas+1;
		old=grade;	
		grade=double.Parse(Console.ReadLine());
	 	total=total+grade;
		if(grade<4)
		{
			fail=fail+1;
		}
	 	if(fail==2)
		{stop="true";}
	 	if(fail==0 & klas==12)
		{stop="true";}
	}
		if(fail==2)
		{
			Console.WriteLine("{0} has been excluded at {1} grade",name, klas-1);
		}
		else{
		Console.WriteLine("{0} graduated. Average grade: {1:0.00}",name, (total/klas));
		}
	}

}
	