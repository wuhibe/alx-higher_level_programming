#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const abc = JSON.parse(body);
    abc.results.forEach(function (item, index, array) {
      array = item.characters;
      array.forEach(function (abc) {
        if (abc.includes('18')) {
          count = count + 1;
        }
      });
    });
    console.log(count);
  }
});
