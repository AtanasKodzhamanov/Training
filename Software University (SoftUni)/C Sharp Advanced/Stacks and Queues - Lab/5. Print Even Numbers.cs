using System;
using System.Collections.Generic;


namespace Stacks_and_Queues___6._Supermarket__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<string> Opashka = new Queue<String>();
            string input = "";
            int end = 0;
            int counter = 0;
            while (end == 0)
            {
               
                input= Console.ReadLine();
                if (input == "End") { 
                    Console.WriteLine(Opashka.Count + " people remaining.");
                    end = 1;
                }
                else if (input=="Paid")
                {
                    int c = Opashka.Count;
                    for(int i = 0; i < c; i++)
                    {
                        Console.WriteLine(Opashka.Dequeue());
                    }
                }
                else
                {
                    Opashka.Enqueue(input);
                }

                counter++;
                if (counter > 100)
                {
                    end = 1;
                }
            }


            }
    }
}
