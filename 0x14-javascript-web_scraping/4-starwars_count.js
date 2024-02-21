#!/usr/bin/node
// script that prints the number of movies where the character 'Wedge Antilles' is present.
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
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
