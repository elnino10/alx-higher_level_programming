#!/usr/bin/node
// Reading from file

// const filesys = require('fs');
// filesys.readFile(process.argv[2], 'utf-8',
//   function (err, data) {
//     if (err) {
//       console.log(err);
//       return;
//     }
//     console.log(data);
//   });

const fs = require('fs');

const filePath = process.argv[2];
try {
  const data = fs.readFileSync(filePath, 'utf-8');
  console.log(data);
} catch (err) {
  console.log(err);
}
