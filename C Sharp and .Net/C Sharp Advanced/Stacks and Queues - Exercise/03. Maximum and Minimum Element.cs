using System;
using System.Collections.Generic;
using System.Linq;

namespace Stacks_and_Queues___4._Fast_Food
{
    class Program
    {
        static void Main(string[] args)
        {
            int quantity= int.Parse(Console.ReadLine());
            int[] orders = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)).ToArray();
            Queue<int> stack = new Queue<int>(orders);
            int counter = 0;
            Console.WriteLine(stack.Max());
            while (stack.Count > 0) {
                counter++;
                int current = stack.Peek();
                
                if (quantity  >= current) { stack.Dequeue(); }
                quantity = quantity - current;
                if (counter > 100) break;
            }
            if (stack.Count() == 0) { Console.WriteLine("Orders complete"); }
            else {
                Console.Write("Orders left:");
                while(stack.Count() > 0)
                {
                    Console.Write(" " + stack.Dequeue());

                }    
              }

        }
    }
}