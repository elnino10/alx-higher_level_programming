#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let firstMax = parseInt(process.argv[2]);
  let secondMax = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    const currArg = parseInt(process.argv[i]);
    if (firstMax > currArg) {
      if (secondMax < currArg) {
        secondMax = currArg;
      } else {
        if (secondMax === firstMax) {
          secondMax = currArg;
        } else {
          continue;
        }
      }
    } else {
      secondMax = firstMax;
      firstMax = currArg;
    }
  }
  console.log(secondMax);
}
