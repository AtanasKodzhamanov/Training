using System;
					
public class Program
{
	public static void Main(){
	int number=int.Parse(Console.ReadLine());
	int newnum=0;
	int sum=0;
		while(sum < number){
		newnum=int.Parse(Console.ReadLine());
		sum=sum+newnum;
		}
Console.WriteLine(sum);
		
	}

}
	