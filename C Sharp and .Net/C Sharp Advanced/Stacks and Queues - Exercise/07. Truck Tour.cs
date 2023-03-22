using System;
using System.Collections.Generic;

namespace Stacks_and_Queues___1._Reverse_Strings__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            var input=Console.ReadLine();
            var stack = new Stack<char>();
            foreach (var character in input)
            {
                stack.Push(character);
            }
            while (stack.Count != 0)
            {
                Console.Write(stack.Pop());
            }
        }
    }
}