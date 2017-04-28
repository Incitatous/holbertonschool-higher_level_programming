#!/usr/bin/node
if (!process.argv[2]) {
    console.log(1);
}
else {
    let res = 0;
    let num =  process.argv[2];
    for (i = process.argv[2]; i > 0; i--) {
        res += num * (num - 1);
        num = num - 1;
    }
    console.log(num)
}
