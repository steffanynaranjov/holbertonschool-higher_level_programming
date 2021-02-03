#!/usr/bin/node
const newVar = process.argv;
if (newVar.length <= 3) {
  console.log('0');
} else {
  newVar.splice(0, 2);
  newVar.sort(function (a, b) { return b - a; });
  console.log(Number(newVar[1]));
}
