#!/usr/bin/node
exports.logMe = (function (item) {
  let counter = 0;
  const clousure = (item) => {
    console.log(`${counter}: ${item}`);
    counter += 1;
  };
  return clousure;
}());
