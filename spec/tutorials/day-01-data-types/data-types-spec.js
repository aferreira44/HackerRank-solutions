var dataTypes = require("../../../tutorials/30-days-of-code/day-01-data-types/data-types")

describe("dataTypes", () => {
  it("should Print the sum of both integers on the first line, the sum of both doubles" +
      " (scaled to  decimal place) on the second line, and then the two concatenated " +
      " strings on the third line.", () => {

    const int = 12
    const double = 4.0
    const string = "is the best place to learn and practice coding!"

    const result = dataTypes.print(int, double, string)

    const exp_firstLine = 16,
          exp_secondLine = 8.0,
          exp_thirdLine = "HackerRank is the best place to learn and practice coding!"

    expect(result).toBe(exp_firstLine + "\n" + exp_secondLine.toFixed(1) + "\n" + exp_thirdLine)
  })
})