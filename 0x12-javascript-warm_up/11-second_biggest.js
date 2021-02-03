#!/usr/bin/node
const newVar = process.argv.slice(2);

if (!newVar.length || newVar.length === 1) {
  console.log('0');
} else {
  console.log(newVar.sort().reverse()[1]);
}
