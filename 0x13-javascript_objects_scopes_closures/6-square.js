#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.char = c;
    if (this.char === undefined) {
      this.char = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(this.char.repeat(this.size));
    }
  }
}
module.exports = Square;
