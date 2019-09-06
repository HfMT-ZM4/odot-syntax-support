// index.js

const convert = require('xml-js');
const fs = require('fs');

const infile = fs.readFileSync('backup-odot.tmLanguage');

var xml =
'<?xml version="1.0" encoding="utf-8"?>' +
'<note importance="high" logged="true">' +
'    <title>Happy</title>' +
'    <todo>Work</todo>' +
'    <todo>Play</todo>' +
'</note>';
var result1 = convert.xml2json(infile, {compact: true, spaces: 4});
//var result2 = convert.xml2json(infile, {compact: false, spaces: 4});

fs.writeFileSync( 'odot-tmLang.json', result1 );


//console.log(result1);

