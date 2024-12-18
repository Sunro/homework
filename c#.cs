using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
        List<int> primes = new List<int>();
        List<int> notPrimes = new List<int>();

        foreach (int i in numbers)
        {
            if (IsPrime(i) && i > 1)
            {
                primes.Add(i);
            }
            else if (i > 1)
            {
                notPrimes.Add(i);
            }
        }

        Console.WriteLine($"Primes: {string.Join(", ", primes)}\nNot Primes: {string.Join(", ", notPrimes)}");
    }

    static bool IsPrime(int a)
    {
        if (a % 2 == 0)
        {
            return a == 2;
        }
        int d = 3;
        while (d * d <= a && a % d != 0)
        {
            d += 2;
        }
        return d * d > a;
    }
}