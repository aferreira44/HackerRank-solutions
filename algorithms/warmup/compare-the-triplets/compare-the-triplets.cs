using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static void Main(String[] args) {

        string[] tokens_a0 = Console.ReadLine().Split(' ');
        int a0 = Convert.ToInt32(tokens_a0[0]);
        int a1 = Convert.ToInt32(tokens_a0[1]);
        int a2 = Convert.ToInt32(tokens_a0[2]);

        int[] scores_a = new int[] {a0, a1, a2};

        string[] tokens_b0 = Console.ReadLine().Split(' ');
        int b0 = Convert.ToInt32(tokens_b0[0]);
        int b1 = Convert.ToInt32(tokens_b0[1]);
        int b2 = Convert.ToInt32(tokens_b0[2]);

        int[] scores_b = new int[] {b0, b1, b2};

        int scoreA = 0;
        int scoreB = 0;

        for (int i = 0; i < scores_a.Length; i++)
        {
            if (scores_a[i] > scores_b[i])
            {
                scoreA++;
            }
            else if (scores_a[i] < scores_b[i])
            {
                scoreB++;
            }
        }

        Console.WriteLine(scoreA + " " + scoreB);
    }
}
