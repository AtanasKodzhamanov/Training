using System;
using System.Collections.Generic;
using System.Linq;

namespace Exam_2___Survivor
{
    class Program
    {
        static void Main(string[] args)
        {
            int rows = int.Parse(Console.ReadLine());

            string[][] jagged = new string[rows][];

            for (int row = 0; row < rows; row++)
            {
                string[] rowvals = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries);
                jagged[row] = new string[rowvals.Length];

                for (int col = 0; col < jagged[row].Length; col++)
                {
                    jagged[row][col] = rowvals[col];
                }
            }
            int collect = 0;
            int opponent = 0;

            while (true)
            {
                string[] command = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries);
                if (command[0] == "Gong") break;
                if (command[0] == "Find")
                {
                    int currow = int.Parse(command[1]);
                    int curcol = int.Parse(command[2]);

                    if (currow >= 0 & currow < rows)
                    {
                        if (jagged[currow].Length > curcol & curcol >= 0)
                        {
                            if (jagged[currow][curcol] == "T")
                            {
                                collect++;
                                jagged[currow][curcol] = "-";
                            }
                        }

                    }

                }

                if (command[0] == "Opponent")
                {
                    int currow = int.Parse(command[1]);
                    int curcol = int.Parse(command[2]);
                    string direction = command[3];
                    int dirr = 0;
                    int dirc = 0;
                    if (currow >= 0 & currow < rows)
                    {
                        if (jagged[currow].Length > curcol & curcol >= 0)
                        {

                            if (jagged[currow][curcol] == "T")
                            {
                                opponent++;
                                jagged[currow][curcol] = "-";

                                if (direction == "down") { dirr = 1; }
                                if (direction == "up") { dirr = -1; }
                                if (direction == "left") { dirc = -1; }
                                if (direction == "right") { dirc = 1; }

                                for (int movecol = 1; movecol <= 3; movecol++)
                                {
                                    for (int moverow = 1; moverow <= 3; moverow++)
                                    {
                                        if (currow + moverow * dirr < rows & currow + moverow * dirr >= 0)
                                        {
                                            if (jagged[currow + moverow * dirr].Length > curcol+movecol * dirc & curcol + movecol * dirc >= 0)
                                            {
                                                if (jagged[currow + moverow * dirr][curcol+ movecol * dirc] == "T")
                                                {
                                                    opponent++;
                                                    jagged[currow + moverow * dirr][curcol+ movecol * dirc] = "-";
                                                }
                                            }
                                        }
                                    }

                                }

                            }
                        }
                    }
                  


                }

            }

            for (int row = 0; row < rows; row++)
            {
                for (int column = 0; column < jagged[row].Length; column++)
                {
                    Console.Write(jagged[row][column] + " ");
                }
                Console.WriteLine();
            }

            Console.WriteLine("Collected tokens: " + collect);
            Console.WriteLine("Opponent's tokens: " + opponent);

        }
    }
}