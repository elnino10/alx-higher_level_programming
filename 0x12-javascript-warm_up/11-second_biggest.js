#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let firstMax = parseInt(process.argv[2]);
  let secondMax = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (firstMax > parseInt(process.argv[i])) {
      if (secondMax < parseInt(process.argv[i])) {
        secondMax = parseInt(process.argv[i]);
      } else {
        continue;
      }
    } else {
      firstMax = parseInt(process.argv[i]);
    }
  }
  console.log(secondMax);
}
