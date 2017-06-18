using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static void Main(String[] args) {
      
        int n = Convert.ToInt32(Console.ReadLine());

        for (int i=0; i < n; i++){
            for (int j=0; j < n; j++){
                if(j < n - i-1){
                    Console.Write(" ");
                }else{
                    Console.Write("#");
                }
            }

            Console.WriteLine("");
        }
    }
}
