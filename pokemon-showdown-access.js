// Required to load pokemon-showdown team functions
const {Teams} = require('pokemon-showdown')

// Required to load pokemon-showdown simulation functions
const Sim = require('pokemon-showdown');

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
    // Generates a team
    case "generate-team":
        var generated_team = Teams.generate("", {seed: [0, 0, 0, 0]})
        console.log(generated_team)
        break;
    // Given a file path containing a team in export format, 
    // turns it into packed format and returns it.
    case "pack-file":
        // Get the team path from arguments
        var team_path = process.argv.at(3);

        var team_str = ''

        // Try to load it.
        try {
            const data = fs.readFileSync(team_path, 'utf-8');
            // Get the text from the file
            team_str = data;
            // Import it as a team
            imported_team = Teams.import(team_str);
            // Pack it into packed format
            packed_team = Teams.pack(imported_team);
            // Spit it back out so it can be read.
            console.log(packed_team);
        } catch (err) {
            console.err(err);
        }
        break;
    case "get-json-of-file":
        // Get the team path from arguments
        var team_path = process.argv.at(3);

        var team_str = ''

        // Try to load it.
        try {
            const data = fs.readFileSync(team_path, 'utf-8');
            // Get the text from the file
            team_str = data;
            // Import it as a team
            imported_team = Teams.import(team_str);
            // Spit it back out so it can be read.
            console.log(imported_team);
        } catch (err) {
            console.err(err);
        }
        break;
    case "sim":
        //printArguments();
        
        // Start a simulation
        stream = new Sim.BattleStream();

        // I think this clears the console, don't really know lol
        (async () => {
            for await (const output of stream) {
                console.log(output);
            }
        })();

        var format_id = process.argv.at(3);
        var player_one_team = process.argv.at(4);
        var player_two_team = process.argv.at(5);
        var player_one_name = process.argv.at(6);
        var player_two_name = process.argv.at(7);
        

        stream.write(`>start {"formatid":"${format_id}"}`)
        stream.write(`>player p1 {"name":"${player_one_name}","team":"${player_one_team}"}`);
        stream.write(`>player p2 {"name":"${player_two_name}","team":"${player_two_team}"}`);

        // We need to check if we have any additional commands
        // Get the number of additional commands
        var num_additional_arguments = process.argv.length - 1 - 7

        // If we have atleast one
        if(num_additional_arguments > 0) {
            // Loop through each
            for (let i = 0; i < num_additional_arguments; i++) {
                // Write each
                stream.write(process.argv.at(i + 7 + 1).replaceAll("|", " "))
            }
        }

        break;

        default:
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
            stream = new Sim.BattleStream();

            (async () => {
                for await (const output of stream) {
                    console.log(output);
                }
            })();


            stream.write('>start {"formatid":"gen6vgc2016"}')
            stream.write(`>player p1 {"name":"Wolfe Glick","team":"${wolfe_2016_packed_team}"}`);
            stream.write(`>player p2 {"name":"Jonathan Evans","team":"${john_2016_packed_team}"}`);
            //stream.write(">p1 team 1256");
            //stream.write(">p2 team 1234");

            // Think of it like this
            // Sky view where p1 is top and p2 is bottom
            // 
            // p1: left     ,     right
            // p2: left     ,     right
            // 
            // This makes a lot of commands.. contextual? I guess?
            //stream.write(`>p1 switch Raichu, move Water Spout`);
            //stream.write('>p2 move Sludge Bomb 2 mega, move Thunder 1');
            break;
}