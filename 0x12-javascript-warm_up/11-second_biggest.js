#!/usr/bin/node
const args = process.argv.slice(2);
function largest (args) {
  let n = args[0];
  for (let i = 1; i < args.length; i++) {
    if (args[i] > n) {
      n = args[i];
    }
  }
  return (n);
}
if (isNaN(args[0])) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const n = largest(args);
  const index = args.indexOf(n);
  args.splice(index, 1);
  console.log(largest(args));
}
