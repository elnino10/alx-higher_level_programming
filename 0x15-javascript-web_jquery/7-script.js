//  script that fetches the character name from this
//  URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data) {
  $('DIV#character').text(data.name);
});
