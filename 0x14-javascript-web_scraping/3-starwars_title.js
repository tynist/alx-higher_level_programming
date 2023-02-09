#!/usr/bin/node
const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
request(starWarsUri, function (error, response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
