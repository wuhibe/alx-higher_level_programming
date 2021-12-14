#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
let x = 0;
if (num) {
  while (x < num) {
    console.log('C is fun');
    x++;
  }
} else {
  console.log('Missing number of occurrences');
}
