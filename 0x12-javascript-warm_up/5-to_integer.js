#!/usr/bin/node
const newVar = process.argv[2];

if (!parseInt(newVar)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${newVar}`);
}
