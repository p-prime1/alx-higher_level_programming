#!/usr/bin/node
const args = process.argv.slice(2);
function fact (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0) {
    return (1);
  }
  return n * fact(n - 1);
}
const n = parseInt(args[0]);
console.log(fact(n));
