#!/usr/bin/node
// Number of films with the given character ID
// const request = require('request');
// let num = 0;

// request.get(process.argv[2], (error, response, body) => {
//   if (error) {
//     console.log(error);
//   } else {
//     const content = JSON.parse(body);
//     content.results.forEach((film) => {
//       film.characters.forEach((character) => {
//         if (character.includes(18)) {
//           num += 1;
//         }
//       });
//     });
//     console.log(num);
//   }
// });

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
