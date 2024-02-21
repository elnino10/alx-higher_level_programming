#!/usr/bin/node
// Reading from file
const fs = require('fs');

const filePath = process.argv[2];
try {
  const data = fs.readFileSync(filePath, 'utf-8');
  console.log(data);
} catch (err) {
  console.log(err);
}
