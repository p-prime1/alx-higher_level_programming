#!/usr/bin/node

request = require('request');

if (process.argv[2]) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  function(error, response, body) {
    /*console.log(error);
    console.log(response);*/
    console.log(body);
  });
}
