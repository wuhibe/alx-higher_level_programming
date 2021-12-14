#!/usr/bin/node

exports.converter = function (base) {
  return function myconverter (num) { return num.toString(base); };
};
