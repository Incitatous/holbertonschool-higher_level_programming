#!/usr/bin/node
var request = require('request');
const url = process.argv[2];
request(url, (err, response) => {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});
