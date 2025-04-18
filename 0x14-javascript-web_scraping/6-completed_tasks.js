#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  content = JSON.parse(body);
  const users = {};
  let i = 1;

  for (const user of content) {
    if (user.completed) {
      users[i] = user.id;
      i += 1;
    }
  }
  console.log(users);
});

