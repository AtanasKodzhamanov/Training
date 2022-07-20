using System;
using System.Linq;
using System.Collections.Generic;

namespace Exam_25_Oct_2020___01._Scheduling
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] tasksinput = Console.ReadLine().Split(", ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();
            int[] threadsinput = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();
            int kill = int.Parse(Console.ReadLine());
            int curthread = 0;
            int curtask = 0;
            Queue<int> threads = new Queue<int>(threadsinput);
            Stack<int> tasks = new Stack<int>(tasksinput);

            while (curtask != kill)
            {
                if (threads.Peek() >= tasks.Peek())
                {
                    curthread = threads.Dequeue();
                    curtask = tasks.Pop();

                    if (curtask == kill) Console.WriteLine("Thread with value " + curthread + " killed task " + curtask);

                }
                else
                {
                    curthread = threads.Dequeue();

                    curtask = tasks.Peek();
                    if (curtask == kill) Console.WriteLine("Thread with value " + curthread + " killed task " + curtask);
                }
                if (curtask == kill)
                {
                    Console.WriteLine(curthread + " " + string.Join(" ", threads));
                }
            }
        }
    }
}
