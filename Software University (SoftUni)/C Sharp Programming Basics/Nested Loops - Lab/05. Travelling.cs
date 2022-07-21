	using System;
using System.Data;
using System.Globalization;
using System.Threading;

public class Program
	{
	public static void Main()
	{
		int etaj = int.Parse(Console.ReadLine());
		int stai = int.Parse(Console.ReadLine());
		string spisak = "";
		string level = "";
		for(int i=etaj;i>0;i--)
        {
			if (i == etaj)
            {
				level = "L";
            }
			else if(i%2==0)
            {
				level = "O";
            }
			else { level = "A"; }

			for(int j=0;j<stai;j++)
            {
				if (j == 0)
				{
					spisak = spisak + level + i.ToString() + j.ToString();
				}
                else
                {
					spisak = spisak + " "+level + i.ToString() + j.ToString();

				}
			}
			Console.WriteLine(spisak);
			spisak = "";
        }
	}
}