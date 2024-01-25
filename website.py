# website.py is the main code to connect the back end code with the front end code and open a local link for the website

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import Roulette as rl
import Craps as cr
import BlackJack as bj

app = Flask(__name__)

balance = 1000

@app.route('/')
def home():
    return render_template('home.html')

# for back button
@app.route('/home')
def returnHome():
    return render_template('home.html')

@app.route('/roulette')
def roulette():
    return render_template('roulette.html')

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html')

@app.route('/craps')
def craps():
    return render_template('craps.html')

@app.route('/get_balance', methods=['GET'])
def get_balance():
    return jsonify({'balance': balance})


if __name__ == '__main__':
    app.run(debug=True)