$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (responseText, textStatus) => {
    if (textStatus === 'success') {
      $('DIV#hello').text(responseText.hello);
    }
  });
});
