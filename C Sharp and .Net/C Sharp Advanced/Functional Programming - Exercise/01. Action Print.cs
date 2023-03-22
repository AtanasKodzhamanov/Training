using System;
using System.Linq;
using System.Collections.Generic;
namespace Functional_Programming___2._Knights_of_Honor
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).ToList().ForEach(x => Console.WriteLine("Sir "+ x));

        }
    }
}