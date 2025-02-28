#!/usr/bin/node

exports.esrever = function (list) {
  const count = list.length;

  for (let i = 0; i < Math.floor(count / 2); i++) {
    const temp = list[i];
    list[i] = list[count - 1 - i];
    list[count - 1 - i] = temp;
  }
  return list;
};
