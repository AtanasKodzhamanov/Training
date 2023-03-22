using System;
using System.Linq;
using System.Collections.Generic;
namespace Functional_Programming___3._Custom_min_function
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToList().Min());
        }
    }
}
