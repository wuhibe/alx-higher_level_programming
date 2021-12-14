#!/usr/bin/node
class Rectangle {
  constructor (weight, height) {
    if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {
      return;
    }
    this.width = weight;
    this.height = height;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
