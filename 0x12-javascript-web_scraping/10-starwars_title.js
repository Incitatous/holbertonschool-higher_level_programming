#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + parseInt(process.argv[2]);
request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
