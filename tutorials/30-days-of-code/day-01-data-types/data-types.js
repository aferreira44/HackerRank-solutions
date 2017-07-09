"use strict";

// Receive the string "Welcome to 30 Days of Code!" as parameter
// and print it after 'Hello, World'

exports.print = (int, double, string) => {
    const i = 4;
    const d = 4.0;
    const s = "HackerRank ";

    const result = i + int + "\n" + (d + double).toFixed(1) + "\n" + s + string;
    return result;
}
