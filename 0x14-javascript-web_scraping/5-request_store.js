#!/usr/bin/node
// script gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

const reqUrl = process.argv[2];
const filePath = process.argv[3];

request.get(reqUrl, (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(filePath, body, 'utf-8', (error) => {
    if (error) console.log(error);
  });
});
