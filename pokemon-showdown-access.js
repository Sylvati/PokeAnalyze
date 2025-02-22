// Required to load pokemon-showdown
const {Teams} = require('pokemon-showdown')

// Required to read files
const fs = require('node:fs');

//Prints out the arguments
function printArguments() {
    process.argv.forEach(function(val, index, array) {
        console.log(index + ': ' + val);
    });
}

// Command processor, used by our python files.
var command = process.argv.at(2)
// Not gonna do any validation, we are using
// code to input here anyway
switch(command) {
    case "generate-team":
        var generated_team = Teams.generate("", {seed: [0, 0, 0, 0]})
        console.log(generated_team)
        break;
}

// Load up wolfe's 2016 worlds team
const wolfe_2016_txt = 'example-teams\\WolfeGlick-worlds-2016.txt'
var wolfe_2016_str = ''

try {
    const data = fs.readFileSync(wolfe_2016_txt, 'utf-8');
    wolfe_2016_str = data
} catch (err) {
    console.err(err);
}

var wolfe_2016_imported_team = Teams.import(wolfe_2016_str);
var wolfe_2016_packed_team = Teams.pack(wolfe_2016_imported_team);

// Load up john's 2016 worlds team
const john_2016_txt = 'example-teams\\JonathanEvans-worlds-2016.txt'
var john_2016_str = ''

try {
    const data = fs.readFileSync(john_2016_txt, 'utf-8');
    john_2016_str = data
} catch (err) {
    console.err(err);
}

var john_2016_imported_team = Teams.import(john_2016_str);
var john_2016_packed_team = Teams.pack(john_2016_imported_team);

// Start a worlds 2016 simulation
const Sim = require('pokemon-showdown');
stream = new Sim.BattleStream();

(async () => {
    for await (const output of stream) {
        console.log(output);
    }
})();


stream.write('>start {"formatid":"gen6vgc2016"}')
stream.write(`>player p1 {"name":"Wolfe Glick","team":"${wolfe_2016_packed_team}"}`);
stream.write(`>player p2 {"name":"Jonathan Evans","team":"${john_2016_packed_team}"}`);
stream.write(">p1 team 1256");
stream.write(">p2 team 1234");

// Think of it like this
// Sky view where p1 is top and p2 is bottom
// 
// p1: left     ,     right
// p2: left     ,     right
// 
// This makes a lot of commands.. contextual? I guess?
stream.write(`>p1 switch Raichu, move Water Spout`);
stream.write('>p2 move Sludge Bomb 2 mega, move Thunder 1');