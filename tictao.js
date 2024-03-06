// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
//   });

//   rl.question('What is your name? ', (name) => {
//     console.log(`Hello, ${name}!`);
//     rl.close();
//   });

const readline = require('readline');


const board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
]



let currentPlayer = 'X';

function printboard(){
    for(let i=0; i++;i<3){
        console.log(`${board[i][0]} ${board[i][1]} ${board[i][2]}`)
    }
}

function checkvin(){
    
}


function play(){

}