$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: lang }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      const lang = $('INPUT#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: lang }, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
