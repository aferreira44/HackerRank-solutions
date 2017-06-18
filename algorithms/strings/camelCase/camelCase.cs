using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static void Main(String[] args) {
        
        string s = Console.ReadLine();
        s = System.Text.RegularExpressions.Regex.Replace(s, "([A-Z])", " $1", System.Text.RegularExpressions.RegexOptions.Compiled).Trim();

        string[] strings = s.Split(' ');
        Console.WriteLine(strings.Length);
    }
}
