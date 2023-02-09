#!/usr/bin/node
// Script prints the title of a Star Wars movie where 
// the episode number matches a given integer.

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
request(starWarsUri, function (error, response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
