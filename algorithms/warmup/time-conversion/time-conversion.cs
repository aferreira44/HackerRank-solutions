using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static void Main(String[] args) {

        string time = Console.ReadLine();

        int h = int.Parse(time.Substring(0,2));
        string ampm = time.Substring(8,2);

        if(ampm == "AM"){

            if (h == 12)
                h = 0;

            Console.Write("0" + h + ":" + time.Substring(3,5));
            
        }else if(ampm == "PM"){

            if (h != 12)
                Console.Write((h+12) + ":" + time.Substring(3,5));
            else
                Console.Write(h + ":" + time.Substring(3,5));
        }
    }
}
