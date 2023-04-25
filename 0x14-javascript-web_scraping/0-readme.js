#!/usr/bin/node
const fs = require('fs');

if (process.argv.length > 2) {
    const filePath = process.argv[2];
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.log(err);
        } else {
            console.log(data);
        }
    });
} else {
    console.log("Please provide a file path as the first argument.");
}
