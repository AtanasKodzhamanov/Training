using System;
using System.Linq;
using System.Collections.Generic;

namespace Sets_and_Dictionaries_2._Sets_of_Elements
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] n = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();

            HashSet<int> set1 = new HashSet<int>();
            HashSet<int> set2 = new HashSet<int>();
            HashSet<int> set3 = new HashSet<int>();
            for (int i = 0; i < n[0]; i++)
            {
                set1.Add(int.Parse(Console.ReadLine()));
            }
            for (int i = 0; i < n[1]; i++)
            {
                set2.Add(int.Parse(Console.ReadLine()));
            }
 

            foreach (int a in set1)
            {
                foreach (int b in set2)
                {
                    if (a == b)
                    {
                        set3.Add(a);
                    }
                }
                
            }
            foreach (int c in set3)
            {
Console.Write(c+ " ");
            }
        }
    }
}