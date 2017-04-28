#!/usr/bin/node
function Fact (number) {
  if (!number || number < 2 || isNaN(number)) {
    console.log(1);
  } else {
    let res = 1;
    for (let num = 1; num <= number; num++) {
      res = res * num;
    }
    console.log(res);
  }
}
Fact(parseInt(process.argv[2]));
