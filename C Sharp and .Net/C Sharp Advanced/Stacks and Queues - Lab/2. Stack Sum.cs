using System;
using System.Collections.Generic;
using System.Linq;

namespace Stacks_and_Queues___3._Simple_Calculator__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine()
               .Split(' ', StringSplitOptions.RemoveEmptyEntries)
               .Reverse()
               .ToArray();

            Stack<string> stack = new Stack<string>(input);

            while (stack.Count>1)
            {
                int a = int.Parse(stack.Pop());
                string command = stack.Pop();
                int b = int.Parse(stack.Pop());

                if (command == "+")
                {
                    stack.Push((a+b).ToString());
                }
                else if (command == "-")
                {
                    stack.Push((a-b).ToString());
                }
                
            }

            Console.WriteLine(stack.Pop());
        }
    }
}