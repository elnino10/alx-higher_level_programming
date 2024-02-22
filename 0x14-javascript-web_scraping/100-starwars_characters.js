#!/usr/bin/node
// script prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) console.log(error);

  body.characters.forEach((char) => {
    request.get(char, { json: true }, (error, response, body) => {
      if (error) console.log(error);
      console.log(body.name);
    });
  });
});
