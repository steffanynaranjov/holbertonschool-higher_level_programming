#!/usr/bin/node
const newVar = parseInt(process.argv[2]);

if (isNaN(newVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < newVar; x++) {
    console.log('C is fun');
  }
}
