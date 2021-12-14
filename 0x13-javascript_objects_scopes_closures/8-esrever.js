#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (const element of list) {
    newList.unshift(element);
  }
  return newList;
};
