#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
console.log(fs.readFile(filePath, 'utf-8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content.trim());
  }
}));
