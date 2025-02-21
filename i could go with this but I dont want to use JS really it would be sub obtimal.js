// Required to load pokemon-showdown
const {Teams} = require('pokemon-showdown')

//Prints out the arguments
/*
process.argv.forEach(function(val, index, array) {
    console.log(index + ': ' + val);
})
*/

switch(process.argv.at(2)) {
    case "generate":
        var generated_team = Teams.generate("", {seed: [0, 0, 0, 0]})
        console.log(generated_team)
        break;
}