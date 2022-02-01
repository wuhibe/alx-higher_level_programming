#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
