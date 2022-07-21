using System;
using System.Linq;
using System.Collections.Generic;


namespace Stacks_and_Queues___5._Print_Even_Numbers__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();
            Queue<int> queue = new Queue<int>(input);

            Queue<int> queue2 = new Queue<int>();

            string output = "";

            while (queue.Count > 0) {
                int current = queue.Dequeue();
                if (current  % 2 == 0)
                {
                    queue2.Enqueue(current);
                }
            }
            Console.Write(string.Join(", ", queue2));
        }
    }
}