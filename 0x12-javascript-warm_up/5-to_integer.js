#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
if (num) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
