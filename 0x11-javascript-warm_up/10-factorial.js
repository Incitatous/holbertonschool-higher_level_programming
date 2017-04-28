#!/usr/bin/node
function Fact (number) {
  if (!process.argv[2] || process.argv[2] < 2 || isNaN(process.argv[2])) {
    console.log(1);
  } else {
    let res = 1;
    for (let num = process.argv[2]; num > 1; num--) {
      res = res * num;
    }
    console.log(res);
  }
}
Fact(parseInt(process.argv[2]));
