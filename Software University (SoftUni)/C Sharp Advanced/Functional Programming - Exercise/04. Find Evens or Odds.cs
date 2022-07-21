using System;
using System.Collections.Generic;


namespace Sets_and_Dictionaries_1._Unique_Usernames
{
    class Program
    {
        static void Main(string[] args)
        {
          int n = int.Parse( Console.ReadLine());
            HashSet<string> set = new HashSet<string>();

            for(int i = 0; i < n; i++)
            {
                set.Add(Console.ReadLine());


            }
            foreach(var c in set)
            {
                Console.WriteLine(c);
            }
        }
    }
}