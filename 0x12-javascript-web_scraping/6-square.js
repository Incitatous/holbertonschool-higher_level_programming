#!/usr/bin/node
const Rectangle = require('./4-rectangle').Rectangle;
/* "call" calls a function with a
given this value and arguments provided individually */
exports.Square = function Square (size) {
    Rectangle.call(this, size, size);
    this.charPrint(c) = function () {
        let res = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c) {
            res += c;
        }
        else {
            res += 'X';
        }
      }
      console.log(res);
      res = '';
}
};
};
