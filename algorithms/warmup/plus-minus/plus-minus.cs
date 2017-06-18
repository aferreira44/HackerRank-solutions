using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static void Main(String[] args) {
      
        int n = Convert.ToInt32(Console.ReadLine());
        string[] arr_temp = Console.ReadLine().Split(' ');
        int[] arr = Array.ConvertAll(arr_temp,Int32.Parse);

        int countP = 0, countN = 0, countZ = 0;

        foreach (int num in arr){
            if(num > 0){
                countP++;
            }else if(num < 0){
                countN++;
            }else{
                countZ++;
            }
        }

        Console.WriteLine(countP/(double)n);
        Console.WriteLine(countN/(double)n);
        Console.WriteLine(countZ/(double)n);
    }
}
