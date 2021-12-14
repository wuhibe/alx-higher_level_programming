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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
