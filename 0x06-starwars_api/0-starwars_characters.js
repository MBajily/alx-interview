#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  if (!characters) {
    console.error('No characters found for the given Movie ID.');
    return;
  }

  // Fetch and print characters' names in order
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, characterBody) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(characterBody).name);
    });
  });
});
