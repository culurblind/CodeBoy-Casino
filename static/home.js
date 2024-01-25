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