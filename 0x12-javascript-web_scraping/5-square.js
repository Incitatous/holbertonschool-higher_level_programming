#!/usr/bin/node
const Rectangle = require('./4-rectangle').Rectangle;
/* "call" calls a function with a
given this value and arguments provided individually */
exports.Square = function Square (size) {
    Rectangle.call(this, size, size);
};
