#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0]);
if (isNaN(num)) {
  console.log('Missing nuber of occurences');
} else {
  let i = 0;
  const str = 'C is fun';
  while (i < num) {
    console.log(str);
    i++;
  }
}
