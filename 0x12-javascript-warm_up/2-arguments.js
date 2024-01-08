#!/usr/bin/node
const { argv } = require('node:process');

let printVal;
if (argv.length < 3) {
  printVal = 'No argument';
} else if (argv.length === 3) {
  printVal = 'Argument found';
} else {
  printVal = 'Arguments found';
}

console.log(printVal);
