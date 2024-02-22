#!/usr/bin/node
// script prints all characters of a Star Wars movie
// Display one character name by line in the same order of the list 'characters' in the /films/ response

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function fetchCharacters () {
  return new Promise((resolve, reject) => {
    request.get(apiUrl, { json: true }, (error, response, body) => {
      if (error) reject(error);
      else resolve(body.characters);
    });
  });
}

function fetchcharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, { json: true }, (error, response, body) => {
      if (error) reject(error);
      else resolve(body);
    });
  });
}

async function printMovieCharacters () {
  try {
    const characters = await fetchCharacters();
    for (const charUrl of characters) {
      const character = await fetchcharacter(charUrl);
      console.log(character.name);
    }
  } catch (err) {
    console.log(err);
  }
}

if (movieId) printMovieCharacters();
