#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((x) => list.indexOf(x) * x);
console.log(list);
console.log(newList);
