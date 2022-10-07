#!/usr/bin/node
const count = process.argv.length;
console.log(count > 3 ? 'Arguments found' : (count === 2 ? 'No arguement' : 'Argument found'));
