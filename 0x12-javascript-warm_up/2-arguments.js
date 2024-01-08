#!/usr/bin/node

let printVal;
if (process.argv.length < 3) {
  printVal = 'No argument';
} else if (process.argv.length === 3) {
  printVal = 'Argument found';
} else {
  printVal = 'Arguments found';
}

console.log(printVal);
