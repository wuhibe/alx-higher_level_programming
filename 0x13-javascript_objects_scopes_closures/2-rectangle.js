#!/usr/bin/node
class Rectangle {
  constructor (weight, height) {
    if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {
      return;
    }
    this.width = weight;
    this.height = height;
  }
}
module.exports = Rectangle;
