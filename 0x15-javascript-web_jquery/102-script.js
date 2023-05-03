$(function () {
  $('#btn_search').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/' + $('#city_search').val() + '%22)&format=json', function (resp, status) {
      if (status === 'success') {
        $('#wind_speed').text(resp.query.results.channel.wind.speed);
      }
    });
  });
});
