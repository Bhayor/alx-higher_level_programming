#!/usr/bin/node
const str = 'C is fun';
if (parseInt(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
