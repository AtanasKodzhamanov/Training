using System;
using System.Collections.Generic;
using System.Linq;

namespace Stacks_and_Queues___2._Basic_queue_operations
{
    class Program
    {
        static void Main(string[] args)
        {

            int N = int.Parse(Console.ReadLine());
            Stack<int> stack = new Stack<int>();

            for (int i = 0; i < N; i++)
            {
                int[] command = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)).ToArray();
                if (command[0] == 1)
                {
                    stack.Push(command[1]);
                }
                if (command[0] == 2)
                {
                    stack.Pop();
                }
                if (command[0] == 3 & stack.Count > 0)
                {
                    Console.WriteLine(stack.Max());
                }
                if (command[0] == 4 & stack.Count > 0)
                {
                    Console.WriteLine(stack.Min());
                }
            }

            while (stack.Count > 1)
            {
                Console.Write(stack.Pop());
                Console.Write(", ");
            }
            if (stack.Count > 0)
            {
                Console.Write(stack.Pop());
            }


        }
    }
}