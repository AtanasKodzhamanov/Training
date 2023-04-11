using System;
using System.Linq;
using System.Collections.Generic;

namespace Stacks_and_Queues_8._Traffic_Light__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            var queue = new Queue<string>();
            var total=0;

            while (true)
            {
                var command = Console.ReadLine();
                if (command == "end") break;
                if (command == "green")
                {
                    for (int i = 0; i < N; i++)
                    {
                        if (queue.Count > 0)
                        {
                            Console.WriteLine(queue.Dequeue()+" passed!");
                            total++;
                        }
                    }
                }
                else queue.Enqueue(command);
            }
            Console.WriteLine($"{total} cars passed the crossroads.");


        }
    }
}

