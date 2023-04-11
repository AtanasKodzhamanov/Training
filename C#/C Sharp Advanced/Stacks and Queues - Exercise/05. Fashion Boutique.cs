using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Stacks_and_Queues___6._Songs_Queue
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(", ", StringSplitOptions.RemoveEmptyEntries).ToArray();
            var playlist = new Queue<string>(input);

            while (true)
            {
                if (playlist.Count == 0) { Console.WriteLine("No more songs!"); break; }
                var command = Console.ReadLine();
                if (command == "Play") playlist.Dequeue();
                else if (command == "Show")
                {

                        Console.WriteLine(string.Join(", ",playlist));

                }
                else 
                {
                    var song = command.Substring(4, command.Length - 4);
                    if (playlist.Contains(song)==false)
                    {
                        playlist.Enqueue(song);
                    }
                    else Console.WriteLine(song + " is already contained!");
                }
            }
        }
    }
}
