const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (body) {
  const result = body.results;
  $.each(result, function (i, field) {
    $('UL#list_movies').append('<li>' + field.title + '</li>');
  });
});
