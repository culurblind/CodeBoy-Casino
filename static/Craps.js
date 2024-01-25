/*
    Craps.py is a python file that runs the back end code for the casino game craps
    it contains functions that print text slowly, clear the terminal, check if an input is a number, and also a method for rolling the dice 
    and the main function where the actual game runs, returning the new balance
*/

function diceTotal() {
    const dice1 = Math.floor(Math.random() * 6) + 1;
    const dice2 = Math.floor(Math.random() * 6) + 1;
    return dice1 + dice2;
}

function craps(balance, bet) {
    let gameplay = true;

    while (gameplay) {
        const diceNum = diceTotal();

        if (diceNum === 7 || diceNum === 11) {
            balance += 2 * bet;
        } else if (diceNum === 2 || diceNum === 3 || diceNum === 12) {
            // Do nothing (balance remains the same)
        } else {
            let pastNumber = false;

            while (!pastNumber) {
                const newNum = diceTotal();

                if (newNum === diceNum) {
                    pastNumber = true;
                    balance += 2 * bet;
                    break;
                } else if (newNum === 7) {
                    balance -= 2 * bet;
                    pastNumber = true;
                    break;
                }
            }
        }
    }

    return balance;
}

