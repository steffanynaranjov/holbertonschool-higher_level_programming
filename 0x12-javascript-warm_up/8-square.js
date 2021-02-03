#!/usr/bin/node
const newVar = parseInt(process.argv[2]);
if (isNaN(newVar)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < newVar; x++) {
    console.log('X'.repeat(newVar));
  }
}
