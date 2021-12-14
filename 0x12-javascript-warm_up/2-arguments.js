#!/usr/bin/node
const argsLen = process.argv.length;
if (argsLen === 2) {
  console.log('No argument');
} else if (argsLen === 3) {
  console.log('Argument found');
} else if (argsLen > 3) {
  console.log('Arguments found');
}
