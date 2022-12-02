from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('home.html')

@application.route('/news')
def news():
    return render_template('news.html')

@application.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@application.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html')

@application.route('/ethereum')
def ethereum():
    return render_template('ethereum.html')

@application.route('/binance')
def binance():
    return render_template('binance.html')

@application.route('/doge')
def doge():
    return render_template('doge.html')

@application.route('/polygon')
def ripple():
    return render_template('polygon.html')

@application.route('/shiba')
def cardano():
    return render_template('shiba.html')

@application.route('/litecoin')
def solana():
    return render_template('litecoin.html')

@application.route('/chainlink')
def terra():
    return render_template('chainlink.html')

@application.route('/bitcoinCash')
def polkadot():
    return render_template('bitcoinCash.html')

@application.route('/algorand')
def avalanche():
    return render_template('algorand.html')

if __name__ == "__main__":
    application.run(debug=True)
