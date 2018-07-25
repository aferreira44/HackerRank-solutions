function main() {
  var n = parseInt(readLine());
  a = readLine().split(' ');
  a = a.map(Number);
  // Write Your Code Here

  const firstElement = 0
  const lastElement = 0

  bubbleSort(a)

  console.log('Array is sorted in ' + numSwaps + ' swaps.')

  console.log('First Element: ' + firstElement)

  console.log('ast Element: ' + lastElement)

}

function bubbleSort(a) {
    for (let i = 0; i < n; i++) {
      // Track number of elements swapped during a single array traversal
      let numberOfSwaps = 0;

      for (let j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
          swap(a[j], a[j + 1]);
          numberOfSwaps++;
        }
      }

      // If no elements were swapped during a traversal, array is sorted
      if (numberOfSwaps == 0) {
        break;
      }
    }
  }