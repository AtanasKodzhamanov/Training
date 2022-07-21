using System;
using System.Linq;
using System.Collections.Generic;

namespace Stacks_and_Queues___1._Basic_Stack_Operations
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] parameters= Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)).ToArray();
            Stack<int> stack = new Stack<int>(Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)));

            for (int i = 0; i < parameters[1]; i++)
            {
                stack.Pop();
            } 
            if (parameters[1]>= parameters[0]) { Console.WriteLine(0); }
            else if (stack.Contains(parameters[2]) == true) { Console.WriteLine("true"); }
            else Console.WriteLine(stack.Min());
           

        }
    }
}