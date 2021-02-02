#!/usr/bin/node
const newVar = process.argv[2];
if (typeof newVar === 'undefined') {
  console.log('No argument');
} else {
  console.log(newVar);
}
