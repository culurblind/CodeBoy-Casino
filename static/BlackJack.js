// Import statements
const random = require('random');
const readlineSync = require('readline-sync');
const clearTerminal = () => console.clear();

// Function to print string slowly
const slowPrint = (inputString, delay = 0.05) => {
    for (const char of inputString) {
        process.stdout.write(char);
        time.sleep(delay);
    }
    console.log();
};

// Function to check if input is not an integer
const isntInt = (rawInput) => isNaN(parseInt(rawInput));

// Cards dictionary
const cards = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
};
const cardKeys = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];

// Function to play Blackjack
const blackJack = (balance) => {
    clearTerminal();
    slowPrint("Welcome to Black Jack!");
    time.sleep(0.5);

    // Game runs while balance is more than 0
    while (balance > 0) {
        time.sleep(2);
        clearTerminal();
        
        // Setting bet
        let placeHolder = true;
        while (placeHolder) {
            slowPrint(`You have a balance of: ${balance}`);
            const bet = readlineSync.question("How much do you want to bet? ");
            clearTerminal();

            if (isntInt(bet)) {
                slowPrint("Please enter a valid integer to bet on.");
            } else if (parseInt(bet) > balance) {
                slowPrint(`Slow your roll there pal, you don't have ${bet}.`);
            } else {
                placeHolder = false;
                const betAmount = parseInt(bet);
                balance -= betAmount;
            }
        }
        
        // Player hand
        console.log();
        const playerHand = [];
        const card1 = cardKeys[random.int(0, 12)];
        const card2 = cardKeys[random.int(0, 12)];
        playerHand.push(card1, card2);
        const card1Val = cards[card1];
        const card2Val = cards[card2];
        let sum = card1Val + card2Val;
        slowPrint(`Player Card: ${card1}`);
        slowPrint(`Player Card: ${card2}`);
        // Double ace case
        if (card1 === "A" && card2 === "A") {
            sum -= 10;
            playerHand.splice(playerHand.indexOf("A"), 1);
        }
        slowPrint(`total = ${sum}`);
        time.sleep(1);

        // Dealer hand
        console.log();
        const dealerHand = [];
        const dealerCard = cardKeys[random.int(0, 12)];
        dealerHand.push(dealerCard);
        const dealerCard1Val = cards[dealerCard];
        let dealerSum = dealerCard1Val;
        slowPrint(`Dealer Card: ${dealerCard}`);

        let turn = false;

        // Case 1 - Blackjack
        if (sum === 21) {
            console.log();
            slowPrint("Black Jack!");
            // Dealer card reveal
            while (dealerSum < 17) {
                const dealerExtraCard = cardKeys[random.int(0, 12)];
                dealerHand.push(dealerExtraCard);
                const dealerExtraCardVal = cards[dealerExtraCard];
                dealerSum += dealerExtraCardVal;
                slowPrint(`Dealer Card: ${dealerExtraCard}`);
                slowPrint(`Dealer total = ${dealerSum}`);
                if ("A" in dealerHand && dealerSum > 21) {
                    dealerSum -= 10;
                    dealerHand.splice(dealerHand.indexOf("A"), 1);
                }
                time.sleep(0.5);
            }
            // Conditionals to determine win, loss, or tie
            if (dealerSum > 21) {
                slowPrint("Dealer Bust");
                balance += 2.5 * betAmount;
                balance = parseInt(balance);
            } else if (dealerSum === 21) {
                slowPrint("Push");
                balance += betAmount;
            } else {
                balance += 2.5 * betAmount;
                balance = parseInt(balance);
            }
        } else {
            // If it is not a Blackjack, give the options
            turn = true;
            let hit = false;
        }

        // Continue the code for the player's turn...
        // ...Continuation of player's turn
        while (turn) {
            console.log();
            const decision = readlineSync.question("stand, hit, double, or split? ");
            console.log();

            // Case 2 - Stand
            if (decision === "stand") {
                // Dealer card reveal
                while (dealerSum < 17) {
                    const dealerExtraCard = cardKeys[random.int(0, 12)];
                    dealerHand.push(dealerExtraCard);
                    const dealerExtraCardVal = cards[dealerExtraCard];
                    dealerSum += dealerExtraCardVal;
                    slowPrint(`dealer's card: ${dealerExtraCard}`);
                    if ("A" in dealerHand && dealerSum > 21) {
                        dealerSum -= 10;
                        dealerHand.splice(dealerHand.indexOf("A"), 1);
                    }
                    slowPrint(`Dealer total = ${dealerSum}`);
                    time.sleep(0.5);
                }
                // Conditionals to determine winner
                if (dealerSum > 21) {
                    slowPrint("Dealer Bust");
                    balance += 2 * betAmount;
                } else if (dealerSum === sum) {
                    slowPrint("Push");
                    balance += betAmount;
                } else if (dealerSum < sum) {
                    slowPrint("You Win!");
                    balance += 2 * betAmount;
                } else if (dealerSum > sum) {
                    slowPrint("Dealer Wins");
                }
                turn = false;
            }

            // Case 2 - Hit
            else if (decision === "hit") {
                // Creating an additional card and append it to the player's hand
                const extraCard = cardKeys[random.int(0, 12)];
                playerHand.push(extraCard);
                slowPrint(`Player Card: ${extraCard}`);
                const extraCardVal = cards[extraCard];
                sum += extraCardVal;
                // Conditionals if the hit makes the total 21 or greater
                if (sum > 21) {
                    if ("A" in playerHand) {
                        sum -= 10;
                        playerHand.splice(playerHand.indexOf("A"), 1);
                    } else {
                        slowPrint("bust");
                        turn = false;
                    }
                }
                slowPrint(`total = ${sum}`);
                if (sum === 21) {
                    const dealerCard = cardKeys[random.int(0, 12)];
                    dealerHand.push(dealerCard);
                    const dealerCardVal = cards[dealerCard];
                    slowPrint(`dealer's card: ${dealerCard}`);
                    dealerSum += dealerCardVal;
                    slowPrint(`dealer total: ${dealerCardVal}`);
                    if (dealerCard === 21) {
                        slowPrint("push");
                        balance += betAmount;
                    } else {
                        slowPrint("you win");
                        balance += 2 * betAmount;
                        balance = parseInt(balance);
                    }
                    turn = false;
                }
                hit = true;
            }

            // Continue the code for double and split...
            // ...Continuation of double and split
            else if (decision === "double") {
                balance -= betAmount;
                // Conditional to make sure the player has enough money to double
                if (balance < 0) {
                    slowPrint("Don't have the money to double");
                    balance += betAmount;
                } else if (hit) {
                    slowPrint("You already hit; you cannot double now");
                } else {
                    betAmount *= 2;
                    slowPrint(balance);
                    console.log();
                    // One extra card for the double
                    const extraCard = cardKeys[random.int(0, 12)];
                    slowPrint(`Player Card: ${extraCard}`);
                    playerHand.push(extraCard);
                    const extraCardVal = cards[extraCard];
                    sum += extraCardVal;
                    time.sleep(0.25);
                    let switchFlag = true;
                    if (sum > 21) {
                        if ("A" in playerHand) {
                            sum -= 10;
                            playerHand.splice(playerHand.indexOf("A"), 1);
                        } else {
                            slowPrint("bust");
                            turn = false;
                            switchFlag = false;
                        }
                    }
                    slowPrint(`total = ${sum}`);
                    console.log();
                    // If no bust then run this code
                    if (switchFlag) {
                        // Dealer card reveal
                        while (dealerSum < 17) {
                            const dealerExtraCard = cardKeys[random.int(0, 12)];
                            dealerHand.push(dealerExtraCard);
                            const dealerExtraCardVal = cards[dealerExtraCard];
                            dealerSum += dealerExtraCardVal;
                            slowPrint(`dealer's card: ${dealerExtraCard}`);
                            if ("A" in dealerHand && dealerSum > 21) {
                                dealerSum -= 10;
                                dealerHand.splice(dealerHand.indexOf("A"), 1);
                            }
                            slowPrint(`Dealer total = ${dealerSum}`);
                            time.sleep(0.5);
                        }
                        // Conditionals to determine winner
                        if (dealerSum > 21) {
                            slowPrint("dealer bust");
                            balance += 2 * betAmount;
                        } else if (dealerSum > sum) {
                            slowPrint("dealer won");
                        } else if (dealerSum < sum) {
                            slowPrint("you win");
                            balance += 2 * betAmount;
                        } else {
                            slowPrint("push");
                            balance += betAmount;
                        }
                        turn = false;
                    }
                }
            }

            // Case 4 - Split
            else if (decision === "split") {
                if (hit) {
                    slowPrint("You already hit; you cannot split now");
                }
                // Runs code only if the 2 cards are the same value
                else if (card1Val === card2Val) {
                    balance -= betAmount;
                    // Won't run split if the money is not enough
                    if (balance < 0) {
                        slowPrint("Don't have the money to split");
                        balance += betAmount;
                    } else {
                        // Getting the other cards for each split
                        slowPrint(`Balance: ${balance}`);
                        console.log();
                        const splitHand1 = [];
                        const splitHand2 = [];
                        splitHand1.push(card1);
                        splitHand2.push(card2);

                        const splitCard1 = cardKeys[random.int(0, 12)];
                        splitHand1.push(splitCard1);
                        const splitCard1Val = cards[splitCard1];
                        let sum1 = card1Val + splitCard1Val;

                        const splitCard2 = cardKeys[random.int(0, 12)];
                        splitHand2.push(splitCard2);
                        const splitCard2Val = cards[splitCard2];
                        let sum2 = card2Val + splitCard2Val;

                        slowPrint(`First split: ${splitCard1}`);
                        slowPrint(`First split total: ${sum1}`);
                        console.log();
                        slowPrint(`Second split: ${splitCard2}`);
                        slowPrint(`Second split total: ${sum2}`);
                        console.log();

                        let splitTurn1 = true;
                        let splitTurn2 = false;
                        let dealerReveal = false;

                        // First split hit and stand
                        while (splitTurn1) {
                            if (sum1 === 21) {
                                dealerReveal = true;
                                splitTurn1 = false;
                                splitTurn2 = true;
                            } else if (sum1 > 21) {
                                slowPrint("First split busts");
                                splitTurn1 = false;
                                splitTurn2 = true;
                            } else {
                                const splitDecision = readlineSync.question("Split 1: hit or stand? ");
                                if (splitDecision === "hit") {
                                    const extraCard1 = cardKeys[random.int(0, 12)];
                                    splitHand1.push(extraCard1);
                                    const extraCard1Val = cards[extraCard1];
                                    sum1 += extraCard1Val;
                                    slowPrint(`Split 1 card: ${extraCard1}`);
                                    if (sum1 > 21) {
                                        if ("A" in splitHand1) {
                                            sum -= 10;
                                            playerHand.splice(playerHand.indexOf("A"), 1);
                                        } else {
                                            slowPrint("Split 1 busts");
                                            splitTurn1 = false;
                                            splitTurn2 = true;
                                        }
                                    }
                                    slowPrint(`Split 1 total = ${sum1}`);
                                    if (sum1 === 21) {
                                        dealerReveal = true;
                                        splitTurn1 = false;
                                        splitTurn2 = true;
                                    }
                                } else if (splitDecision === "stand") {
                                    dealerReveal = true;
                                    splitTurn1 = false;
                                    splitTurn2 = true;
                                }
                                console.log();
                            }

                            // Second split hit or stand
                            while (splitTurn2) {
                                if (sum2 === 21) {
                                    dealerReveal = true;
                                    splitTurn2 = false;
                                } else if (sum2 > 21) {
                                    slowPrint("Second split busts");
                                    splitTurn2 = false;
                                } else {
                                    const splitDecision = readlineSync.question("Split 2: hit or stand? ");
                                    if (splitDecision === "hit") {
                                        const extraCard2 = cardKeys[random.int(0, 12)];
                                        splitHand2.push(extraCard2);
                                        const extraCard2Val = cards[extraCard2];
                                        sum2 += extraCard2Val;
                                        slowPrint(`Split 2 card: ${extraCard2}`);
                                        if (sum2 > 21) {
                                            if ("A" in splitHand2) {
                                                sum -= 10;
                                                playerHand.splice(playerHand.indexOf("A"), 1);
                                            } else {
                                                slowPrint("Split 2 busts");
                                                splitTurn2 = false;
                                            }
                                        }
                                        slowPrint(`Split 2 total = ${sum2}`);
                                        if (sum2 === 21) {
                                            dealerReveal = true;
                                            splitTurn2 = false;
                                        }
                                    } else if (splitDecision === "stand") {
                                        dealerReveal = true;
                                        splitTurn2 = false;
                                    }
                                    console.log();
                                }
                            }

                            // Dealer card reveal
                            if (dealerReveal) {
                                while (dealerSum < 17) {
                                    const dealerExtraCard = cardKeys[random.int(0, 12)];
                                    dealerHand.push(dealerExtraCard);
                                    const dealerExtraCardVal = cards[dealerExtraCard];
                                    dealerSum += dealerExtraCardVal;
                                    console.log();
                                    slowPrint(`Dealer's card: ${dealerExtraCard}`);
                                    if ("A" in dealerHand && dealerSum > 21) {
                                        dealerSum -= 10;
                                        dealerHand.splice(dealerHand.indexOf("A"), 1);
                                    }
                                    slowPrint(`Dealer total = ${dealerSum}`);
                                    time.sleep(0.5);
                                }

                                // Determine winner
                                if (dealerSum > 21) {
                                    slowPrint("Dealer Bust!");
                                    if (sum1 <= 21) {
                                        balance += betAmount;
                                    }
                                    if (sum2 <= 21) {
                                        balance += 2 * betAmount;
                                    }
                                } else {
                                    if (dealerSum > sum1) {
                                        slowPrint("First split loses");
                                    } else if (dealerSum < sum1) {
                                        slowPrint("First split wins");
                                        balance += 2 * betAmount;
                                    } else {
                                        slowPrint("First split pushes");
                                        balance += betAmount;
                                    }

                                    if (dealerSum > sum2) {
                                        slowPrint("Second split loses");
                                    } else if (dealerSum < sum2) {
                                        slowPrint("Second split wins");
                                        balance += 2 * betAmount;
                                    } else {
                                        slowPrint("Second split pushes");
                                        balance += betAmount;
                                    }
                                }

                                turn = false;
                            }
                        }
                    }
                } else {
                    slowPrint("Your cards are not the same; you cannot split");
                }
            }
        }

        console.log();
        const status = readlineSync.question("Do you want to play again? (y/n) ");
        let statusLoop = true;

        while (statusLoop) {
            if (status === "y") {
                statusLoop = false;
            } else if (status === "n") {
                statusLoop = false;
                slowPrint("Thanks for playing BlackJack!");
                return balance;
            } else {
                slowPrint("Type y or n");
            }
        }
    }

    if (balance <= 0) {
        slowPrint("You are out of money!");
    }

    return balance;
};
