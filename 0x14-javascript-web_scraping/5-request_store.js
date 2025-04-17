#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];
if (url) {
  request(url, function (error) {
    if (error) {
      console.error(error);
    }
  })
    .pipe(fs.createWriteStream(filePath, 'utf-8', 'w'));
}
