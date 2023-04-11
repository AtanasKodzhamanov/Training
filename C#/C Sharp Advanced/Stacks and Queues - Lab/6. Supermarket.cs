using System;
using System.Linq;
using System.Collections.Generic;

namespace Stacks_And_Queues___7._Hot_Potato__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] circle = Console.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries).ToArray();
            int turns = int.Parse(Console.ReadLine());
            int limit = 10000000;

            Queue<string> opashka = new Queue<string>(circle);
            string removed = "";
            int end = 0;
            while (end==0)
            {
                for (int i = 1; i < turns; i++)
                {
                   
                    opashka.Enqueue(opashka.Dequeue());
                    
                }
                if (opashka.Count > 1)
                {
                    Console.WriteLine("Removed " + opashka.Dequeue());
                }
                if (opashka.Count == 1)
                {
                    Console.WriteLine("Last is " + opashka.Dequeue());
                }

                if (opashka.Count == 0) { end = 1; }
            }





        }
    }
}
