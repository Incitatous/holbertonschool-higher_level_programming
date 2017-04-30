#!/usr/bin/node
/* this keyword refers to the current
object the code is being written inside */
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
};
