const url = 'https://www.fourtonfish.com/hellosalut/';
$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code');
    $.get(`${url}?lang=${lang.val()}`, (data, textStatus) => {
      if (textStatus === 'success' && lang.val()) {
        $('DIV#hello').html(data.hello);
      }
    });
  });
});
