using System;
using System.Collections.Generic;
using System.Linq;


namespace Stacks_and_Queues___5._Fashion_Boutique
{
    class Program
    {
        static void Main(string[] args)
        {
           
            int[] clothesinabox = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)).ToArray();
            Stack<int> stack = new Stack<int>(clothesinabox);
            int capacity = int.Parse(Console.ReadLine());
            int total = 0;
            int racks = 0;

            int capacityleft = capacity;
            while (stack.Count > 0)
            {
                if (capacityleft >= stack.Peek())
                {
                    capacityleft = capacityleft - stack.Pop();
                }
                else
                {
                    capacityleft = capacity;
                    racks++;
                }
            }
 

            Console.WriteLine(racks+1);
        }
    }
}
