var operators = require("../../../tutorials/30-days-of-code/day-02-operators/operators")

describe("operators", () => {
  it("should Print 'The total meal cost is ' + totalCost + ' dollars.', where totalCost is the" +
      "rounded integer result of the entire bill",
  () => {

    const mealCost = 12.00;
    const tipPercent = 20;
    const taxPercent = 8;

    const result = operators.print(mealCost, tipPercent, taxPercent);

    expect(result).toBe("The total meal cost is 15 dollars.");
  })
})