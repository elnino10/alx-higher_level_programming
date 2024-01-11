#!/usr/bin/node
const dict = require('./101-data').dict;

const invert = {};
for (const key in dict) {
  if (invert[dict[key]] === undefined) {
    invert[dict[key]] = [];
  }
  invert[dict[key]].push(key);
}
console.log(invert);
