$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (responseText, textStatus) => {
  if (textStatus) {
    $('div#character').text(responseText.name);
  }
});
