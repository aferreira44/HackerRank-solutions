"use strict";

// Print "The total meal cost is " + totalCost + " dollars.", where totalCost is the
// rounded integer result of the entire bill

exports.print = (mealCost, tipPercent, taxPercent) => {
  const tip = mealCost * (tipPercent / 100);
  const tax = mealCost * (taxPercent / 100);

  const totalCost = Math.round(mealCost + tip + tax);

  const result = "The total meal cost is " + totalCost + " dollars.";
  return result;
}
