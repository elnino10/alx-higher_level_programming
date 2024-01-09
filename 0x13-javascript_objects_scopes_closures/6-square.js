#!/usr/bin/node

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let row = 0; row < this.height; row++) {
        let char = '';
        for (let column = 0; column < this.width; column++) {
          char += c;
        }
        console.log(char);
      }
    }
  }
}

module.exports = Square;
