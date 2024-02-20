#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: node read_file.js <file_path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(`An error occurred: ${error}`);
  } else {
    console.log(data);
  }
});
