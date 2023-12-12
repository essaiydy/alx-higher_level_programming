#!/usr/bin/node
if (parseInt(process.argv[2])) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
}

if (isNaN(process.argv[2])) {
  console.log('Not a number');
}
