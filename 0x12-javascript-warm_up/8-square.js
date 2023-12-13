#!/usr/bin/node
let width = parseInt(process.argv[2]);

if (isNaN(process.argv[2]))
	{
		console.log('Missing size');
	}
if (width)
	{
		for(let i = 0; i < width; i++){
			let row = '';
			for(let j = 1; j <= width; j++){
				row += 'x';
			} console.log(row);
		}
	}
