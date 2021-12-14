#!/usr/bin/node
exports.callMeMoby = (number, _function) => {
  for (let i = 0; i < number; i++) {
    _function();
  }
};
