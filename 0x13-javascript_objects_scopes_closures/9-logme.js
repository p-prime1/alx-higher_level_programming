#!/usr/bin/node

exports.logMe = (function (item) {
  let log = 0;
  return function (item) {
    console.log(`${log}: ${item}`);
    log++;
  };
})();
