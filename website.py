# website.py is the main code to connect the back end code with the front end code and open a local link for the website

from flask import Flask, render_template
import programs.Roulette as rl
import programs.Craps as cr
import programs.BlackJack as bj

app = Flask(__name__)

balance = 1000

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/roulette')
def roulette():
    # Call the function/method that runs the roulette game
    result = rl.roulette(balance)
    return render_template('roulette.html', result=result)

@app.route('/blackjack')
def blackjack():
    # Call the function/method that runs the blackjack game
    result = bj.blackjack(balance)
    return render_template('blackjack.html', result=result)

@app.route('/craps')
def craps():
    # Call the function/method that runs the craps game
    result = cr.craps(balance)
    return render_template('craps.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)