const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(url, function (result) {
  $('DIV#character').append(result.name);
});
