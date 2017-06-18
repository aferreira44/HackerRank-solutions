using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static void Main(String[] args) {

        string[] tokens_n = Console.ReadLine().Split(' ');

        int n = Convert.ToInt32(tokens_n[0]);
        int k = Convert.ToInt32(tokens_n[1]);
        
        string[] a_temp = Console.ReadLine().Split(' ');
        int[] a = Array.ConvertAll(a_temp,Int32.Parse);

        int sum = 0;

        for(int i=0;i < n;i++){
            for(int j=0; j < n; j++){
                if(i < j && (a[i] + a[j]) % k == 0){
                    sum++;
                }
            }
        }

        Console.WriteLine(sum);
    }
}
