$.get('https://swapi-api.hbtn.io/api/films/?format=json', (responseText, textStatus) => {
  if (textStatus) {
    $('ul#list_movies').append(...responseText.results.map(movie => `<li>${movie.title}</li>`));
  }
});
