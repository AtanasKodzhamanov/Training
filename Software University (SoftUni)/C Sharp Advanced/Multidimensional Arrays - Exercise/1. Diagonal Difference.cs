using System;
using System.Linq;

namespace Multidimensional_Arrays___2._2X2_Squares_in_a_Matrix
{
    class Program
    {
        static void Main(string[] args)
        {

            int[] dimensions = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();
            int cubes = 0;
            char[,] matrix = new char[dimensions[0], dimensions[1]];
            for (int row = 0; row < dimensions[0]; row++)
            {
                char[] rows = Console.ReadLine().Split(" ",StringSplitOptions.RemoveEmptyEntries).Select(char.Parse).ToArray();

                for (int column = 0; column < dimensions[1]; column++)
                {
                    matrix[row, column] = rows[column];
                }
            }

            for (int row = 0; row <= dimensions[0] - 2; row++)
            {
                for (int column = 0; column <= dimensions[1] - 2; column++)
                {
                    if (matrix[row, column] == matrix[row + 1, column] &&
                       matrix[row, column] == matrix[row + 1, column + 1] &&
                       matrix[row, column] == matrix[row, column + 1])
                    {
                        cubes++;
                    }
                }
            }
            Console.WriteLine(cubes);
        }
    }
}
