using System;
using System.Collections.Generic;
using System.Linq;

namespace Stacks_and_Queues___4._Matching_Brackets__Lab_
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            Stack<int> stack = new Stack<int>() ;

            for (int i= 0; i < input.Length;i++)
            {
                if (input[i] == '(')
                {
                    stack.Push(i);
                }
                if (input[i]==')')
                {
                    int start=stack.Pop();
                    Console.WriteLine(input.Substring(start,i-start+1));
                }

            }




        }




    }
}
