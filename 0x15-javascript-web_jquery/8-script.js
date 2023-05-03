$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    encode: 'true'
  })
    .done((data) => {
      const movies = data.results;
      movies.forEach(movie => {
        const title = movie.title;
        $('#list_movies').append(`<li>${title}</li>`);
      });
    });
});
