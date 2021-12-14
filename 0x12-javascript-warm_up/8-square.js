#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
let x = 0;
let line = '';
if (num) {
  for (let j = 0; j < num; j++) {
    line += 'X';
  }
  while (x < num) {
    console.log(line);
    x++;
  }
} else {
  console.log('Missing size');
}
