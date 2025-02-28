#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    const chars = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(chars.repeat(this.width));
    }
  }
}

module.exports = Square;
