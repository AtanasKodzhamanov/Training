using System;
using System.Linq;
using System.Collections.Generic;


namespace Sets_and_Dictionaries___3._Periodic_Table
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            SortedSet<string> set = new SortedSet<string>();
            string[] input;

            for (int i = 0; i < n; i++)
            {
                input = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).ToArray();
                for (int j = 0; j < input.Length; j++)
                {
                    set.Add(input[j]);
                    
                }
            }
            Console.WriteLine(string.Join(' ', set));
        }
    }
}
