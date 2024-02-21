#!/usr/bin/node
// script writes a string to a file
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];
try {
  fs.writeFileSync(filePath, content, 'utf-8');
} catch (err) {
  console.log(err);
}
