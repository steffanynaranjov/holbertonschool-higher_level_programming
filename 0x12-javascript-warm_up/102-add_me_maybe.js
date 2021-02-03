#!/usr/bin/node
exports.addMeMaybe = function (newVar, theFunction) {
  theFunction(++newVar);
};
