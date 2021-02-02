#!/usr/bin/node
const newVar = process.argv.length;
if (newVar === 2) {
  console.log('No argument');
} else if (newVar === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
