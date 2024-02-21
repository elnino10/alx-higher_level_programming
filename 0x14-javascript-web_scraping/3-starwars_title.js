#!/usr/bin/node
// Star Wars
const request = require('request');

const movieId = process.argv[2];
const urlEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(urlEndpoint, (error, response, body) => {
  if (error) console.log(error);
  const jsonData = JSON.parse(body);
  console.log(jsonData.title);
});
