import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/explore')
def explore():
    BTCGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'BTCGraph.png')
    ETHGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'ETHGraph.png')
    BNBGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'BNBGraph.png')
    XRPGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'XRPGraph.png')
    ADAGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'ADAGraph.png')
    SOLGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'SOLGraph.png')
    LUNAGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'LUNAGraph.png')
    AVAXGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'AVAXGraph.png')
    DOGEGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'DOGEGraph.png')
    DOTGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'DOTGraph.png')
    return render_template('explore.html', BTCGraph = BTCGraph, ETHGraph = ETHGraph, BNBGraph = BNBGraph, XRPGraph = XRPGraph, ADAGraph = ADAGraph,
                           SOLGraph = SOLGraph, LUNAGraph = LUNAGraph, AVAXGraph = AVAXGraph, DOGEGraph = DOGEGraph, DOTGraph = DOTGraph)

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html')

@app.route('/ethereum')
def ethereum():
    return render_template('ethereum.html')

@app.route('/binance')
def binance():
    return render_template('binance.html')

@app.route('/doge')
def doge():
    return render_template('doge.html')

@app.route('/polygon')
def ripple():
    return render_template('polygon.html')

@app.route('/shiba')
def cardano():
    return render_template('shiba.html')

@app.route('/litecoin')
def solana():
    return render_template('litecoin.html')

@app.route('/chainlink')
def terra():
    return render_template('chainlink.html')

@app.route('/bitcoinCash')
def polkadot():
    return render_template('bitcoinCash.html')

@app.route('/algorand')
def avalanche():
    return render_template('algorand.html')

if __name__ == "__main__":
    app.run(debug=True)
