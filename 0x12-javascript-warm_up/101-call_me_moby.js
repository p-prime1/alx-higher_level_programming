#!/usr/bin/node
exports.callMeMoby = function (num, newFunc) {
  const newNum = parseInt(num);
  let i = 0;
  while (i < newNum) {
    newFunc();
    i+=1
  }
};
