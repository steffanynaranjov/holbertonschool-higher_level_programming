#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let newVar = 0; newVar < x; newVar++) {
    theFunction();
  }
};
