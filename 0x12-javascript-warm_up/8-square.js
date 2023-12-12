#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (Number.isInteger(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
