#!/usr/bin/node
function factorial (a) {
  return a < 1 || isNaN(a) ? 1 : a * factorial(a - 1);
}
console.log(factorial(Number(process.argv[2])));
