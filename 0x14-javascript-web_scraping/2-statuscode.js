#!/usr/bin/node

const request = require('request');
if (process.argv[2]) {
  request(process.argv[2], (error, response) => {
    console.error(`code: ${error}`);
    console.log(`code: ${response.statusCode} `);
  });
}
