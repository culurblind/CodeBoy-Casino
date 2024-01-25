/*
    home.js runs the front end code by making the buttons work and updating the balance after every game is done
*/

function handleButtonClick(url) {
    
    window.location.href = url;
}

document.addEventListener('DOMContentLoaded', function () {
    updateBalance();

    // Add event listeners for buttons and actions

    function updateBalance() {
        // Make an API request to the backend to get the updated balance
        fetch('/get_balance')
            .then(response => response.json())
            .then(data => {
                // Update the balance display
                document.getElementById('balance counter').innerText = 'Balance: ' + data.balance;
            })
            .catch(error => console.error('Error fetching balance:', error));
    }

    // Add other functions and logic for your game and UI interactions
});

// First, make a letiable to get the button that submits the data.
let sliderBTN = document.getElementById("sliderBTN");
let sliderInp = document.getElementById("money");

// Then, add the event listener for clicking, which will fire the GET request to the server, and then print the output
// from the user when the GET request gets a response
sliderBTN.addEventListener('click', () => {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            // make a pop up with my response text
            document.getElementById("outputArea").innerText = (xhr.responseText);
        }
    }

    let sliderData = sliderInp.value;
    let gameType = "Roulette";
    let dataType = "Bet Amount";
    // this line below here, the url needs to be edited 
    xhr.open('GET', `/game_type/${gameType}/data_type/${dataType}/raw_data/${sliderData}`, true);
    xhr.send(null);
});


// First, make a variable to get the button that submits the data.
let goBTN = document.getElementById("goBTN");
let text = document.getElementsByTagName("textarea")[0];
// Then, add the event listener for clicking, which will fire the GET request to the server, and then print the output
// from the user when the GET request gets a response
goBTN.addEventListener('click', () => {
    let xhr2 = new XMLHttpRequest();
    xhr2.onreadystatechange = function() {
        if (xhr2.readyState == XMLHttpRequest.DONE) {
            // make a pop up with my response text
            document.getElementById("outputArea").innerText = (xhr2.responseText);
        }
    }

    let textData = text.value;
    let gameType = "Poker";
    let dataType = "MYBETTTT";
    // this line below here, the url needs to be edited 
    xhr2.open('GET', `/game_type/${gameType}/data_type/${dataType}/raw_data/${textData}`, true);
    xhr2.send(null);
});
