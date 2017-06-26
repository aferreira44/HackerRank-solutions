// Receive the string "Welcome to 30 Days of Code!" as parameter
// and print it after 'Hello, World'

exports.print = inputString => {
    const result = "Hello, World.\n" + inputString
    return result
}
