using System;
using System.Collections.Generic;
using System.Linq;

namespace Stacks_and_Queues___7._Truck_Tour
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            var petrol= new Queue<int>();
            var distance = new Queue<int>();
            var index = new Queue<int>();
            var thispetrol = 0;

            var petrol2 = petrol;
            var distance2 = distance;
            var complete = 1;
            for (int i = 0; i < N; i++) 
            { 
               int[] input = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();
                petrol.Enqueue(input[0]);
                distance.Enqueue(input[1]);
                index.Enqueue(i);
            }

            for (int i = 0; i < N; i++)
            {
                for(int j = 0; j< N; j++)
                {
                    var curp = petrol.Dequeue();
                    petrol.Enqueue(curp);
                    var curd = distance.Dequeue();
                    distance.Enqueue(curd);
                    thispetrol = thispetrol + curp - curd;
                    if (thispetrol < 0) { complete = 0; }

                }
                if (complete==1) { Console.WriteLine(i); break; }
                complete = 1;
                thispetrol = 0;
                petrol.Enqueue(petrol.Dequeue());
                distance.Enqueue(distance.Dequeue());
            }


        }
    }
}