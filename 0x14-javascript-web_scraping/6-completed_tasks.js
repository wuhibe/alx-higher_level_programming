#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const list = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const abc = JSON.parse(body);
    abc.forEach(function (item, index, array) {
      if (item.completed) {
        if (list[item.userId] === undefined) {
          list[item.userId] = 1;
        } else {
          list[item.userId]++;
        }
      }
    });
    console.log(list);
  }
});
