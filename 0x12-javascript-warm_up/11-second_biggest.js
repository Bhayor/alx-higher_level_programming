#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const nuArr = process.argv.slice(2).map(Number);
  const secBig = nuArr.sort(function (a, b) { return b - a; })[1];
  console.log(secBig);
}
