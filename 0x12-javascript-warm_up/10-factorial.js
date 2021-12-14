#!/usr/bin/node
const process = require('process');
const x = parseInt(process.argv[2]);
function factorial (num) {
  if (num > 1) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}
console.log(factorial(x));
