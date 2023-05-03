$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json',
    encode: 'true'
  })
    .done((data) => {
      $('#character').text(data.name);
    });
});
