const fs = require('fs');
const xml2js = require('xml2js');
const parser = new xml2js.Parser();
const yaml = require('js-yaml');

// CSV
fs.readFile('../me.csv', 'utf8', (err, data) => {
    if (err) throw err;

    // Split the CSV data into rows
    const rows = data.split('\n');

    // Get the header row and split it into columns
    const headers = rows[0].trim().split(',');

    // Remove the header row from the rows array
    rows.shift();

    // Parse the remaining rows into objects
    const results = rows.map((row) => {
        const values = row.trim().split(',');
        const obj = {};
        headers.forEach((header, i) => {
            obj[header] = values[i];
        });
        return obj;
    });

    console.log(results);
});

// JSON
fs.readFile('../me.json', 'utf8', (err, data) => {
    if (err) throw err;
    const obj = JSON.parse(data);
    console.log(obj);
});

// XML
fs.readFile('../me.xml', 'utf8', (err, data) => {
    if (err) throw err;
    parser.parseString(data, (err, result) => {
        if (err) throw err;
        console.log(result['me']);
        console.log(result['me']['hobbies']);
    });
});

// YAML
fs.readFile('../me.yaml', 'utf8', (err, data) => {
    if (err) throw err;
    const obj = yaml.load(data);
    console.log(obj);
});

// TXT
fs.readFile('../me.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
});



