#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let firstMax = parseInt(process.argv[2]);
  let secondMax = firstMax;
  for (let i = 2; i < process.argv.length; i++) {
    if (firstMax > parseInt(process.argv[i])) {
      if (secondMax < parseInt(process.argv[i])) {
        secondMax = parseInt(process.argv[i]);
      } else {
        continue;
      }
    } else {
      secondMax = firstMax;
      firstMax = parseInt(process.argv[i]);
    }
  }
  console.log(secondMax);
}
