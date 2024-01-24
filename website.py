from flask import Flask, render_template
import Roulette as rl
import Craps as cr
import BlackJack as bj

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/roulette')
def roulette():
    result = rl.roulette(1000)
    return render_template('roulette.html', result = result)

@app.route('/blackjack')
def blackjack():
    result = bj.blackJack(1000)
    return render_template('blackjack.html', result = result)

@app.route('/craps')
def craps():
    result = cr.craps(1000)
    return render_template('craps.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)