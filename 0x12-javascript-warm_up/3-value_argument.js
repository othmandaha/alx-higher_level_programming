#!/usr/bin/node
const args = process.argv;
let i = 0;

while (args[i] !== undefined) {
  i++;
}

if (i < 3) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
