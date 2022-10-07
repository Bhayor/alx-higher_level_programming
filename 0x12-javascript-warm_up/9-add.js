#!/usr/bin/node
const f = parseInt(process.argv[2]);
const l = parseInt(process.argv[3]);
if (isNaN(f) && isNaN(l)) {
  console.log('NaN');
} else {
  add(f, l);
}

function add (a, b) {
  console.log(a + b);
}
