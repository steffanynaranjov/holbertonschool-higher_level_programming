#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
request(url, (error, response, content) => {
  if (!error) {
    const people = JSON.parse(content).characters;
    people.forEach((character) => {
      request(character, (error, response, content) => {
        if (!error) {
          console.log(JSON.parse(content).name);
        }
      });
    });
  }
});
