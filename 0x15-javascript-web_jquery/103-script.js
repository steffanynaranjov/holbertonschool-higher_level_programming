$(document).ready(function () {
  $('INPUT#btn_translate').on('click', translate);
  $('INPUT#language_code').on('keypress', (enter) => {
    if (enter.which == 13) {
      translate();
    }
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  const lang = $('INPUT#language_code');
  $.get(`${url}?lang=${lang.val()}`, (data, textStatus) => {
    if (textStatus === 'success' && lang.val()) {
      $('DIV#hello').html(data.hello);
    }
  });
}
