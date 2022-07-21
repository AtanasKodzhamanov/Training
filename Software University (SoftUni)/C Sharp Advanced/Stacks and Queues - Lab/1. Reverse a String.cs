using System;
using System.Collections.Generic;
using System.Linq;

namespace Stacks_and_Queues___2._Stack_Sum__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine()
                .Split(' ',StringSplitOptions.RemoveEmptyEntries);
            Stack<string> stack = new Stack<string>(input);
           

            int stop = 0;
            int loop = 0;
            while (stop != 1)
            {
                loop++;
                if (loop > 100) { stop = 1; }
                string[] command = Console.ReadLine().ToLower().Split(' ', StringSplitOptions.RemoveEmptyEntries);
                if (command[0] == "add")
                {
                    stack.Push(command[1]);
                    stack.Push(command[2]);
                }
                else if (command[0] == "remove")
                {
                    for (int i = 0; i < int.Parse(command[1]) ; i++)
                    {
                        if (stack.Count() >= int.Parse(command[1])) { stack.Pop(); }
                    }
                }
               if (command[0] == "end")
                {
                    stop = 1;
                }
            }
            int sum = 0;
                foreach(var ch in stack)
                {
                    sum = sum + int.Parse(ch);
                }
                Console.WriteLine("Sum: " + sum);
        }
    }
}