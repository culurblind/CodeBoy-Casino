from flask import Flask, render_template
import Roulette as rl
import Craps as cr
import BlackJack as bj

app = Flask(__name__)

balance = 1000

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/roulette')
def roulette():
    result = rl.roulette(balance)
    return render_template('roulette.html', result = result)

@app.route('/blackjack')
def blackjack():
    result = bj.blackJack(balance)
    return render_template('blackjack.html', result = result)

@app.route('/craps')
def craps():
    result = cr.craps(balance)
    return render_template('craps.html', result = result)

# We need to make code to make the balance accesible by the JS file
#@app.route('/')
#def index():
#    balance = balance
#    return render_template('index.html', balance=balance)

if __name__ == '__main__':
    app.run(debug=True)