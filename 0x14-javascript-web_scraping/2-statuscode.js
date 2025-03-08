#!/usr/bin/node

const request = require('request');
if (process.argv[2]) {
  request(process.argv[2], (response) => {
    console.log(`code: ${response} `);
  });
}
