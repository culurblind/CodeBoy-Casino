from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
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

if __name__ == '__main__':
    app.run(debug=True)