#!/usr/bin/node
// Number of films with the given character ID
const request = require('request');

const urlEndpoint = process.argv[2];
request.get(urlEndpoint, (error, response, body) => {
  if (error) console.log(error);
  const jsonData = JSON.parse(body);
  let count = 0;
  jsonData.results.forEach(el => {
    el.characters.forEach(el => {
      if (el.endsWith('18/')) count++;
    });
  });
  console.log(count);
});
