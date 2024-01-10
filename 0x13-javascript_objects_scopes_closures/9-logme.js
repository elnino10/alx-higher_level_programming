#!/usr/bin/node

let numPrints = 0;
exports.logMe = function (item) {
  console.log(numPrints + ': ' + item);
  numPrints++;
};
