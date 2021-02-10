#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
const orderDict = {};
request(url, (error, response, content) => {
  if (!error) {
    const people = JSON.parse(content).characters;
    people.forEach((character) => {
      request(character, (error, response, content) => {
        if (!error) {
          orderDict[character.split('/')[5]] = JSON.parse(content).name;
          if (Object.entries(orderDict).length === people.length) {
            Object.values(orderDict).forEach((element) => {
              console.log(element);
            });
          }
        }
      });
    });
  }
});
