#!/usr/bin/node
const process = require('process');
if (process.argv[2]) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
