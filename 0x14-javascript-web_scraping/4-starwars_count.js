#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;
  for (const film of films) {
    if (film.characters.includes(characterUrl)) {
      count++;
    }
  }
  console.log(count);
});
