using System;
using System.Linq;

namespace Multidimensional_Arrays___3._Maximal_Sum
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] dimensions = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();
            
            int summax = 0;
            int sum = 0;
            int rowmax = 0;
            int columnmax = 0;
            //Read in matrix
            
            int[,] matrix = new int[dimensions[0], dimensions[1]];
            for (int row = 0; row < dimensions[0]; row++)
            {
                int[] rows = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();

                for (int column = 0; column < dimensions[1]; column++)
                {
                    matrix[row, column] = rows[column];
                }
            }
            //End

            for (int row = 0; row < dimensions[0]-2; row++)
            {
                for (int column = 0; column < dimensions[1]-2; column++)
                {
                    sum = matrix[row, column] +
                         matrix[row + 1, column] +
                         matrix[row + 2, column] +
                         matrix[row, column + 1] +
                         matrix[row + 1, column + 1] +
                         matrix[row + 2, column + 1] +
                         matrix[row, column + 2] +
                         matrix[row + 1, column + 2] +
                         matrix[row + 2, column + 2];
                   if (sum > summax)
                    {
                        summax = sum;
                        sum = 0;
                        rowmax = row;
                        columnmax = column;
                    }
                }
            }

            Console.WriteLine("Sum = "+summax);

            for (int row = rowmax; row < rowmax+3; row++)
            {
                for (int column = columnmax; column < columnmax+3; column++)
                {
                    Console.Write(matrix[row, column] + " ") ;
                }
                Console.WriteLine();
            }



        }
    }
}