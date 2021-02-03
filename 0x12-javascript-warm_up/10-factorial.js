#!/usr/bin/node
function factorial (newVar) {
  if (newVar <= 1 | !newVar) {
    return 1;
  } else {
    return factorial(newVar - 1) * newVar;
  }
}

const newVar = Number(process.argv[2]);

console.log(factorial(newVar));
