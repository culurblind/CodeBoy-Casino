/*
    Craps.py is a python file that runs the back end code for the casino game craps
    it contains functions that print text slowly, clear the terminal, check if an input is a number, and also a method for rolling the dice 
    and the main function where the actual game runs, returning the new balance
*/

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to print string slowly
// Default delay of 0.1s if no delay parameter is given
const slowPrint = (inputString, delay = 0.05) => {
    for (const char of inputString) {
        process.stdout.write(char);
        wait(delay * 1000);
    }
    console.log();
};

// Function to simulate waiting
const wait = (milliseconds) => {
    const start = new Date().getTime();
    let end = start;
    while (end < start + milliseconds) {
        end = new Date().getTime();
    }
};

// Function to check if input is an integer
const isntInt = (rawInput) => isNaN(rawInput) || !Number.isInteger(parseFloat(rawInput));

// Function to roll dice and return the total
const diceTotal = () => {
    const dice1 = Math.floor(Math.random() * 6) + 1;
    const dice2 = Math.floor(Math.random() * 6) + 1;
    return dice1 + dice2;
};

// Main Craps function
const craps = (balance) => {
    slowPrint("Welcome to Craps! Your goal is to see whether the dice will roll a winning number.");
    slowPrint("In the first round, if you roll a 7 or 11, you win. If you roll a 2, 3, or 12, you automatically lose.");
    slowPrint("Any other combination of values will be added to the point, and you will continue rerolling until you get that number again or roll a 7, in which you lose");
    console.log();
    wait(3000);

    let gameplay = true;
    while (gameplay) {
        let placeHolder = true;
        while (placeHolder) {
            slowPrint("You have a balance of: " + balance);
            const bet = readline.question("How much do you want to bet? ");
            if (isntInt(bet) || parseInt(bet) <= 0 || !Number.isSafeInteger(parseInt(bet))) {
                slowPrint("Please enter a valid positive integer to bet on.");
            } else if (parseInt(bet) > balance) {
                slowPrint("Slow your roll there pal, you don't have " + bet + ".");
            } else {
                placeHolder = false;
                const betAmount = parseInt(bet);
                balance -= betAmount;
            }
        }

        const diceNum = diceTotal();
        readline.question("Alright, betting " + betAmount + ". Press enter to roll.");
        slowPrint("Rolling... Rolling... Rolling... ", 0.1);

        if (diceNum === 7 || diceNum === 11) {
            slowPrint("The dice rolled " + diceNum + ", You won!");
            balance += 2 * betAmount;
        } else if (diceNum === 2 || diceNum === 3 || diceNum === 12) {
            slowPrint("You lost the bet, the dice rolled " + diceNum);
        } else {
            console.log("You rolled " + diceNum + " the die will reroll");
            let pastNumber = false;

            while (!pastNumber) {
                readline.question("Press enter to roll.");
                slowPrint("Rolling... Rolling... Rolling... ", 0.1);
                const newNum = diceTotal();
                if (newNum === diceNum) {
                    slowPrint("You rerolled " + diceNum + " again! You win!");
                    pastNumber = true;
                    balance += 2 * betAmount;
                    break;
                } else if (newNum === 7) {
                    slowPrint("You rolled a 7! You have lost the game");
                    balance -= 2 * betAmount;
                    pastNumber = true;
                    break;
                } else {
                    slowPrint("You rolled, " + newNum + " the dice will roll again");
                }
            }

            slowPrint("Your balance is now: " + balance);
        }

        let statusLoop = true;

        while (statusLoop) {
            const status = readline.question("Do you want to play again? (y/n) ");
            if (status.toLowerCase() === "y") {
                statusLoop = false;
            } else if (status.toLowerCase() === "n") {
                gameplay = false;
                statusLoop = false;
                slowPrint("Thanks for playing craps!");
            } else {
                slowPrint("That is not a valid input.");
            }
        }

        if (balance <= 0) {
            slowPrint("You are out of money!");
            gameplay = false;
        }
    }

    return balance;
};