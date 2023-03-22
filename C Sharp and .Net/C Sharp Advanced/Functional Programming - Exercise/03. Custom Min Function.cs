using System;
using System.Linq;
using System.Collections.Generic;

namespace Functional_Programming___4._Find_evens_or_odds
{
    class Program
    {
        static void Main(string[] args)
        {

            int[] range = Console.ReadLine().Split(" ",StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();
            var results = new List<int>();
            string command = Console.ReadLine();

            Predicate<int> predicate = command == "odd"
                ? x=> x % 2 != 0
                : new Predicate<int>((x) => x % 2 == 0);
        
            for(int i=range[0];i<=range[1];i++)
            {
                if (predicate(i))
                {
                    results.Add(i);
                }
            }

            Console.WriteLine(string.Join(" ", results));
        }
    }
}
