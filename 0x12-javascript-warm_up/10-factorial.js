#!/usr/bin/node

const arg = parseInt(process.argv[2]);
function factorial (n) {
  if (n <= 1 || isNaN(arg)) {
    return 1;
  }
  return (n * factorial(n - 1));
}

console.log(factorial(arg));
