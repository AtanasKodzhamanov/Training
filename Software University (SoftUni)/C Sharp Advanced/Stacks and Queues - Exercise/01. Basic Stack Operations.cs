using System;
using System.Collections.Generic;
using System.Linq;

namespace Stacks_and_Queues___2._Basic_queue_operations
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] parameters = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)).ToArray();
            Queue<int> stack = new Queue<int>(Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)));

            for (int i = 0; i < parameters[1]; i++)
            {
                stack.Dequeue();
            }
            if (parameters[1] >= parameters[0]) { Console.WriteLine(0); }
            else if (stack.Contains(parameters[2]) == true) { Console.WriteLine("true"); }
            else Console.WriteLine(stack.Min());


        }
    }
}