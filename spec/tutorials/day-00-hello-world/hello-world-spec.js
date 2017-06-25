var helloWorld = require("../../../tutorials/30-days-of-code/day-00-hello-world/hello-world")

describe("helloWorld", () => {
  it("should print Hello, World after Welcome to 30 Days of Code!", () => {
    
    const inputString = 'Welcome to 30 Days of Code!'

    const result = helloWorld.processData(inputString)
    expect(result).toBe("Hello, World.\n" + inputString)
  })
}) 