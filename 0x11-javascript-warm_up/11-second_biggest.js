#!/usr/bin/node
let myArr = [];
for (let i = 2; process.argv[i]; i++) {
  myArr.push(process.argv[i]);
}
let sortedArr = myArr.sort();
sortedArr.pop();
console.log(sortedArr.pop());
/*
if (!process.argv[2] || !process.argv[3]) { console.log(0); } else {
  let secMax = -Infinity;
  let Max = -Infinity;
  for (let i = 2; process.argv[i]; i++) {
    if (process.argv[i] > Max) {
      Max = process.argv[i];
    }
    if (process.argv[i] > secMax && process.argv[i] !== Max) {
      secMax = process.argv[i];
    }
  }
  console.log(secMax);
}
*/
