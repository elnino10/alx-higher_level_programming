// script that fetches and lists the title for all movies by using
// this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  const results = data.results;
  for (const result of results) {
    $('UL#list_movies').append(`<li>${result.title}</li>`);
  }
});
